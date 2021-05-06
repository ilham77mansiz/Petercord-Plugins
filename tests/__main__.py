# All rights reserved.

import os

from petercord import petercord


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../userge/plugins/unofficial") else 'main'
    await userge.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    userge.begin(_worker())
    print('userge test has been finished!')
