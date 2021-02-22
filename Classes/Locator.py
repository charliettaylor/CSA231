import re


class Locator():
    '''
    takes an SRL(str) as a parameter 
    '''

    def __init__(self, SRL: str) -> None:
        try:
            if type(SRL) == str:
                self.SRL = SRL
            else:
                raise ValueError
        except ValueError:
            print("SRL must be a string")

        format = re.compile('^[a-z]*://[\w.]*[/\w]*')
        check = format.search(self.SRL)
        assert check.group() == self.SRL

    def srl(self) -> str:
        '''
        returns the entire SRL represented by a locator
        '''
        return self.SRL

    def kind(self) -> str:
        '''
        returns the locator's kind
        '''
        return self.SRL.split('://')[0]

    def location(self) -> str:
        '''
        returns a string representing the locator's location
        '''
        return self.SRL.split('/')[2]

    def location_parts(self) -> list:
        '''
        returns a list of strings representing the parts of a locator's
        location
        '''
        return self.location().split('.')

    def resource(self) -> str:
        '''
        returns the locator's resource
        '''
        cut = self.SRL.split('//')
        cut = cut[-1].removeprefix(self.location())
        return cut

    def resource_parts(self) -> list:
        '''
        returns a list of strings representing the parts of a locator's
        resource
        '''
        return self.SRL.split('/')[3:]

    def parent(self) -> 'Locator':
        '''
        returns a new Locator object where the last resource part has been
        removed
        '''
        if len(self.resource_parts()) > 1:
            return Locator(self.SRL[:self.SRL.rfind('/')])
        else:
            return Locator(self.SRL)

    def within(self, resource_part: str) -> 'Locator':
        '''
        returns a new Locator object where the given resource part is
        appended to the end of the SRL
        '''
        return Locator(self.SRL + '/' + resource_part)


def test_Locator():
    ex = 'wicked://xylo.yeet.zoo/a123/buck/cuck/d123'
    test = Locator(ex)

    def test_srl():
        assert type(test.srl()) == str

    def test_kind():
        assert type(test.kind()) == str

    def test_location():
        assert type(test.location()) == str

    def test_location_parts():
        assert type(test.location_parts()) == list

    def test_resource():
        assert type(test.resource()) == str

    def test_resource_parts():
        assert type(test.resource_parts()) == list

    def test_parent():
        assert type(test.parent()) == Locator

    def test_within():
        assert type(test.within('e')) == Locator
        test.within('e').srl() == (test.srl() + 'e')

    test_srl()
    test_kind()
    test_location()
    test_location_parts()
    test_resource()
    test_resource_parts()
    test_parent()
    test_within()

test_Locator()
