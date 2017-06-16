import xml.etree.ElementTree as ET
with open('example2.xml', 'rt') as f:
    tree = ET.parse(f)

root = tree.getroot()

tag = '{http://www.tei-c.org/ns/1.0}'

#insert error catchers

for child in root:
        for lower in child:
                #print(lower.tag)
                #find name
                try:
                        for titleStmt in lower.findall(tag + 'titleStmt'):
                                #print(titleStmt.tag)
                                result = titleStmt.find(tag + 'title').text
                                print(result)
                except:
                        print('error')
        for abstract_parent in child:
                #find abstract
                try:
                        for abstract_elem in abstract_parent.findall(tag + 'abstract'):
                                abstract_result = abstract_elem.find(tag + 'p').text
                                print(abstract_result)
                except:
                        print('error no abstract_result')

        for publication_date in child:
                #find publication date
                try:
                        for publicationStmt in publication_date.findall(tag + 'publicationStmt'):
                                date_result = publicationStmt.find(tag + 'date').text
                                print(date_result)
                except:
                        print('no publication date')
        for version_parent in child:
                #find version name
                try:
                        for version_child in version_parent.findall(tag + 'appInfo'):
                                for version in version_child:

                                        version_result = version.get('ident')
                                        print(version_result)
                #find versionTime
                                        version_time_result = version.get('when')
                                        print(version_time_result)
                except:
                                        print('no version time and version date')

        for authors_parent in child:
                for authors_child in authors_parent:

                        for biblStruct in authors_child:

                                for analytic in biblStruct:
                                        for author in analytic:

                                                #get name
                                                for persName in author.findall(tag + 'persName'):
                                                        try:
                                                                for name_result in persName.getchildren():
                                                                        print(name_result.text)
                                                                
                                                        except:
                                                                print('no name')

                                                #get affiliation
                                                for affiliation in author.findall(tag + 'affiliation'):

                                                                for affiliation_result in affiliation.getchildren():
                                                                        print(affiliation_result.text)
                                                                #get address
                                                                for address in affiliation.findall(tag + 'address'):
                                                                        for address_result in address.getchildren():
                                                                                print(address_result.text)


                                                #get email
                                                for email in author.findall(tag + 'email'):

                                                        print(email.text)
                                                
                                                #notes
                                                #surname = persName.find(tag + 'surname').text
                                                        #something.append(firstname)
                                                        #print(something)
                                                        #forme.get('type') middlename in persName:
                                                                #firstname = persName.find(tag + 'forename').text
                                                                #middlename = persName.find(tag + 'forename').text where middlename.get('type') == 'middle'
                                                                #print(firstname, middlename)
                                                                #print('1')
                                                                #surname = persName.find(tag + 'surname').text
                                                                #firstname = persName.find(tag + 'forename').text
                                                                #print(firstname, surname)
                                                '''
                                                        try:
                                                                for middlename in persName:
                                                                        middle = middlename.get('type')
                                                                        if middle == 'middle':
                                                                                namelist = []
                                                                                for x in range(0, 2):
                                                                                        namelist.append(firstname)
                                                                                print('first and middle')
                                                        except:
                                                                print('no')
                                                for orgName in author.findall(tag + 'affiliation'):
                                                        org_type = orgName.find(tag + 'orgName').text
                                                        print(org_type)
                                                        #rganization = orgName.find(tag + 'orgName').text
                                                        #print(organization)
                                                '''

