class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


emails = input()
valid_domain = ['com', 'bg', 'org', 'net']
while emails != 'End':

    if len(emails.split('@')[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    elif '@' not in emails:
        raise MustContainAtSymbolError('Email must contain @')

    elif emails.split('.')[1] not in valid_domain:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    emails = input()

    print('Email is valid')