from typing import Optional

from app.integrations.dashamail.exceptions import DashamailSubscriptionFailed, DashamailUnsubscriptionFailed
from app.integrations.dashamail.http import DashamailHTTP


class AppDashamail:
    def __init__(self) -> None:
        self.http = DashamailHTTP()

    def subscribe_user(self, list_id: str, email: str, first_name: str, last_name: str, tags: Optional[list[str]] = None) -> None:
        payload = {
            'method': 'lists.add_member',
            'update': True,
            'list_id': list_id,
            'email': email,
            'merge_1': first_name,
            'merge_2': last_name,
        }

        if tags:
            payload['merge_3'] = ';'.join(tags)

        response = self.http.post(
            url='',
            payload=payload,
        )

        if response['response']['msg']['err_code'] != 0:
            raise DashamailSubscriptionFailed(f'{response}')

    def unsubscribe_user(self, email: str) -> None:
        response = self.http.post(
            url='',
            payload={
                'method': 'lists.unsubscribe_member',
                'email': email,
            },
        )

        if response['response']['msg']['err_code'] != 0:
            raise DashamailUnsubscriptionFailed(f'{response}')


__all__ = [
    'AppDashamail',
]
