
'''          CODE BY  𐏓꯭  𝗠𝗥ᬊ͜͡  M A LEGEND 〆͎          '''

import urllib.parse
import os
from data import MAIL_SUBJECTS, MAIL_CC, MAIL_BCC, MAIL_TEXT
from colors import Colors

def send_whatsapp_mail(version_key, target_number):
    try:
        subject = MAIL_SUBJECTS[version_key]
        cc = MAIL_CC[version_key]
        bcc = MAIL_BCC[version_key]
        body = MAIL_TEXT[version_key].format(target_number)

        mailto_link = (
            f"mailto:support@whatsapp.com"
            f"?subject={urllib.parse.quote(subject)}"
            f"&cc={urllib.parse.quote(','.join(cc))}"
            f"&bcc={urllib.parse.quote(','.join(bcc))}"
            f"&body={urllib.parse.quote(body)}"
        )

        # Open the default mail app with the constructed mailto link
        os.system(f'termux-open-url "{mailto_link}"')
        Colors.typing_effect("Opening your mail app...", Colors.GREEN + Colors.BOLD)

    except KeyError:
        Colors.typing_effect("Invalid version selected. Please choose a valid version key.", Colors.RED + Colors.BOLD)
    except Exception as e:
        Colors.typing_effect(f"An error occurred: {str(e)}", Colors.RED + Colors.BOLD)