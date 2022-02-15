from django.db.models.signals import post_save
from django.dispatch import receiver
from donor.models import Donor
from post_office.models import EmailTemplate
from post_office import mail
# from mipweb.utils import send_message
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from donor.models import Donor


@receiver(post_save, sender=Donor)
def create_message(sender, instance, created, **kwargs):
    if created:
        donor = Donor.objects.create(sponsor=instance)

        if donor:
            tpl_name = 'donor_acknowledgement'
            msg_subject = 'Your donation pledge received'
            donor_name = donor.name
            donor_email = donor.email
            msg_bag = """
                            Dear {{ donor_name }}, thank for your donation pledge
                            towards our Research Trust Fund. You will let us know 
                            when you send the said fund.

                            We are grateful.

                            Yours sincerely,
                            ACS-ERC Team
                        """
            #send_message(tpl_name, msg_subject, msg_bag, donor_email, donor_name, 'mivieux@yahoo.com')

            mail.send(
                    ['{{ donor_email }}'],
                    'mivieux@yahoo.com',
                    template='welcome_email',
                    context={'Recipient': '{{ donor_name }}'},
                    priority='now',
            )

# Utility function for sending email
def send_message(tplName: str,
                 mip_subject: str,
                 msg_content: str,
                 rxer_email: str,
                 rxer_name: str,
                 txer_email: str,
                 ):
    # Create an email instance
    EmailTemplate.objects.create(
        name=tplName,
        subject=mip_subject,
        content=msg_content,
    )

    mail.send(
        rxer_email,
        txer_email,
        template=tplName,
        context={'name': rxer_name},
    )

