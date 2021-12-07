import vobject
import pandas as pd


def read_vcf(path):
    with open(path, 'r') as f:
        vcard = vobject.readOne(f.read())
        return {vcard.contents['fn'][0].value: [email.value for email in vcard.contents['email']]}

with open("contatos.vcf", "r") as contatos:
    ctts = read_vcf(contatos)

print(ctts)

