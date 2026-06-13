"""feed.md を Gmail/Workspace SMTP でメール送信する(ローカル実行用)。

AI を必要としない処理。OAuth に依存せず git と Python だけで完結する。
認証は local/.env または環境変数 GMAIL_APP_PASSWORD から読む。
"""
import os
import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage
from smtplib import SMTPAuthenticationError

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEED = os.path.join(BASE, "feed.md")
ENV = os.path.join(BASE, "local", ".env")


def load_env():
    if not os.path.exists(ENV):
        return
    with open(ENV, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def main():
    load_env()
    password = os.environ.get("GMAIL_APP_PASSWORD")
    if not password:
        sys.exit("GMAIL_APP_PASSWORD が未設定。local/.env か環境変数で設定してください。")

    mail_from = os.environ.get("NEWS_MAIL_FROM", "").strip()
    if not mail_from:
        sys.exit("NEWS_MAIL_FROM が未設定。Gmail アカウントを設定してください。")
    mail_to = os.environ.get("NEWS_MAIL_TO", mail_from).strip() or mail_from

    if not os.path.exists(FEED):
        sys.exit(f"feed.md が見つかりません: {FEED}")
    with open(FEED, encoding="utf-8") as f:
        body = f.read()
    if not body.strip():
        sys.exit("feed.md が空です。送信を中止します。")

    msg = EmailMessage()
    msg["Subject"] = f"技術ニュース要約 {datetime.now():%Y-%m-%d}"
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg.set_content(body)

    # 465(implicit SSL)はブロックされる環境があるため 587(STARTTLS)を使う。
    # local_hostname を明示しないと getfqdn() がスペース入りの値を返し
    # EHLO がプロトコル違反になる環境があるため固定する。
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, local_hostname="localhost", timeout=30) as smtp:
            smtp.starttls()
            smtp.login(mail_from, password)
            smtp.send_message(msg)
    except SMTPAuthenticationError:
        sys.exit(
            "SMTP 認証に失敗しました。NEWS_MAIL_FROM が App Password 発行元の Gmail と一致しているか、"
            "GMAIL_APP_PASSWORD が正しいか確認してください。"
        )
    print(f"sent to {mail_to}")


if __name__ == "__main__":
    main()
