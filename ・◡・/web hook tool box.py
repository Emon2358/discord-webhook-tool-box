import requests
import json
def display_menu():
    print("")
    print("▄███▄   █▀▄▀█ ████▄    ▄   ")
    print("█▀   ▀  █ █ █ █   █     █  ")
    print("██▄▄    █ ▄ █ █   █ ██   █ ▀░▀▀")
    print("█▄   ▄▀ █   █ ▀████ █ █  █ ")
    print("▀███▀      █        █  █ █ ")
    print("          ▀         █   ██ ")
    print("                                     ")
    print("                                      Made by emon2358")

    print('[1] メッセージ')
    print('[2] 埋め込みメッセージ')
    print('[3] メディア送信')
    print('[4] urlメッセージ')
    print('[5] ユーザーメンション')
    print('[6] チャンネルメンション')

def send_message():
    while True:
        display_menu()
        webhook_url = input("Webhook URLを入力してください: ")
        message_type = input("送信するメッセージの形式を選択してください：(1-6): ")

        if message_type == "1" or message_type == "2":
            message = input("送信するメッセージを入力してください: ")
            payload = {
                "content": message
            }

            if message_type == "2":
                embed_title = input("埋め込みメッセージのタイトルを入力してください: ")
                embed_description = input("埋め込みメッセージの説明を入力してください: ")

                payload["embeds"] = [
                    {
                        "title": embed_title,
                        "description": embed_description,
                        "color": 3447003
                    }
                ]
        elif message_type == "3":
            sub_message_type = input("送信するメディアの種類を選択してください：(1-2): ")
            if sub_message_type == "1":
                media_url = input("送信する画像のURLを入力してください: ")
                payload = {
                    "embeds": [
                        {
                            "image": {
                                "url": media_url
                            }
                        }
                    ]
                }
            elif sub_message_type == "2":
                media_url = input("送信する動画のURLを入力してください: ")
                payload = {
                    "embeds": [
                        {
                            "video": {
                                "url": media_url
                            }
                        }
                    ]
                }
            else:
                print("無効な選択です。1か2を選択してください。")
                continue
        elif message_type == "4":
            link_title = input("リンクのタイトルを入力してください: ")
            link_url = input("リンクのURLを入力してください: ")
            payload = {
                "content": f"[{link_title}]({link_url})"
            }
        elif message_type == "5":
            user_id = input("メンションするユーザーのIDを入力してください: ")
            payload = {
                "content": f"<@{user_id}>"
            }
        elif message_type == "6":
            channel_id = input("メンションするチャンネルのIDを入力してください: ")
            payload = {
                "content": f"<#{channel_id}>"
            }
        else:
            print("無効な選択です。1から6の数字を選択してください。")
            continue

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 204:
            print("メッセージが正常に送信されました。")
        else:
            print(f"メッセージの送信に失敗しました。エラーコード: {response.status_code}")

        another_message = input("別のメッセージを送信しますか？ (y/n): ")
        if another_message.lower() != "y":
            break

if __name__ == "__main__":
    send_message()