import xml.etree.ElementTree as ET
tree = ET.parse('example2.xml')
root = tree.getroot()

tag = '{http://www.tei-c.org/ns/1.0}'
#get game
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
                                        print(version_result.tag)
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

                                                for persName in author.findall(tag + 'persName'):


                                                        firstname = persName.find(tag + 'forename').text
                                                        surname = persName.find(tag + 'surname').text
                                                         print('first name only')

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
