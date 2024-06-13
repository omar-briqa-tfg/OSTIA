from enum import Enum
from typing import Dict
from user_agents import parse


class DeviceType(Enum):
    PC = 'PC'
    MOBILE = 'MOBILE'
    TABLET = 'TABLET'

    BOT = 'BOT'
    EMAIL_CLIENT = 'EMAIL_CLIENT'

    UNKNOWN = '-'


def browser_info(user_agent: str) -> Dict[str, any]:
    ua_string = parse(user_agent)

    is_automatic = ua_string.is_bot or ua_string.is_email_client

    device_type = (DeviceType.PC.value if ua_string.is_pc else
                   DeviceType.BOT.value if ua_string.is_bot else
                   DeviceType.TABLET.value if ua_string.is_tablet else
                   DeviceType.MOBILE.value if ua_string.is_mobile else
                   DeviceType.EMAIL_CLIENT.value if ua_string.is_email_client else DeviceType.UNKNOWN.value)

    device = ua_string.get_device()
    browser = ua_string.get_browser()
    operating_system = ua_string.get_os()

    result = {
        'OS': operating_system,
        'browser': browser,
        'device': device,
        'device_type': device_type,
        'is_automatic': str(is_automatic)
    }

    return result
