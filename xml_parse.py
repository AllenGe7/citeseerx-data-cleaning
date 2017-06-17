import xml.etree.ElementTree as ET
import os

file = 'example2.xml'
with open(file, 'rt') as f:
    tree = ET.parse(f)

root = tree.getroot()

basetag = os.path.basename(os.path.normpath(file))
print (basetag)

tag = '{http://www.tei-c.org/ns/1.0}'
#get game
#insert error catchers

volumeBoolean = False
pageBoolean = False
issueBoolean = False
ordnum = 0
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
                                                        #get name
                                                        try:
                                                                ordnum = ordnum + 1
                                                                print(ordnum)
                                                                name_result = []
                                                                for name_final in persName.getchildren():
                                                                        name_result.append(name_final.text)
                                                                print(', '.join(name_result))
                                                        except:
                                                                print('no name')
                                                        #get affiliation
                                                        for affiliation in author.findall(tag + 'affiliation'):
                                                                affiliation_result = []

                                                                for affiliation_final in affiliation.findall(tag + 'orgName'):

                                                                        affiliation_result.append(affiliation_final.text)

                                                                print(', '.join(affiliation_result))
                                                                #get address
                                                                address_result = []

                                                                for address in affiliation.findall(tag + 'address'):
                                                                        for address_final in address.getchildren():
                                                                                address_result.append(address_final.text)
                                                                print(', '.join(address_result))
                                                        #get email
                                                        for email in author.findall(tag + 'email'):
                                                                print(email.text)
                                                for biblScope in author.findall(tag + 'biblScope'):
                                                        volume_match = {'unit': 'volume'}
                                                        issue_match = {'unit': 'issue'}

                                                        if (volume_match == biblScope.attrib):
                                                                volume_result = biblScope.text
                                                                print(volume_result)
                                                                volumeBoolean = True
                                                        if (issue_match == biblScope.attrib):
                                                                issue_result = biblScope.text
                                                                print(issue_result)
                                                                issueBoolean = True
                                                        if (biblScope.get('unit') == 'page'):
                                                                page_from = biblScope.get('from')
                                                                page_to = biblScope.get('to')
                                                                page_result = page_from + ' '+ page_to
                                                                print(page_result)
                                                                pageBoolean = True
                                                        if (issueBoolean and volumeBoolean):
                                                                print('print to number table')



                                                        #surname = persName.find(tag + 'surname').text

