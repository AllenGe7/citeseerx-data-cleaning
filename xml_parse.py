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
                                                        if (biblScope.get('unit') == 'page'):
                                                                if (biblScope.text == None):
                                                                        Page_from = biblScope.get('from')
                                                                        Page_to = biblScope.get('to')
                                                                        Page_result = Page_from + ' ' + Page_to
                                                                        print(Page_result)
                                                                else:
                                                                        print(biblScope.text)
                                                        elif (biblScope.get('unit') == 'volume'):
                                                                if (biblScope.text == None):
                                                                        Volume_from = biblScope.get('from')
                                                                        Volume_to = biblScope.get('to')
                                                                        Volume_result = Volume_from + ' ' + Volume_to
                                                                        print(Volume_result)
                                                                else:
                                                                        print(biblScope.text)
                                                        elif (biblScope.get('unit') == 'volume'):
                                                                if (biblScope.text == None):
                                                                        Volume_from = biblScope.get('from')
                                                                        Volume_to = biblScope.get('to')
                                                                        Volume_result = Volume_from + ' ' + Volume_to
                                                                        print(Volume_result)
                                                                else:
                                                                        print(biblScope.text)

for teiHeader in root:

        for front in teiHeader:
                for div in front:
                        for listBibl in div:
                                for biblStruc in listBibl:
                                        for analytic in biblStruc.findall(tag + 'analytic'):
                                                for title in analytic.findall(tag + 'title'):
                                                        #print(title.text)
                                                        print('')
                                                for title in analytic.findall(tag + 'author'):

                                                        for persName in title:
                                                                refName_result = []
                                                                for refName in persName.getchildren():

                                                                        refName_result.append(refName.text)
                                                                print(', '.join(refName_result))
                                        for monogr in biblStruc.findall(tag + 'monogr'):
                                                for imprint in monogr:

                                                        for refInfo in imprint.findall(tag + 'biblScope'):


                                                                refVolume_match = {'unit': 'volume'}

                                                                if (refInfo.get('unit') == 'page'):

                                                                        if (refInfo.text == None):
                                                                                refPage_from = refInfo.get('from')
                                                                                refPage_to = refInfo.get('to')
                                                                                refPage_result = refPage_from + ' ' + refPage_to
                                                                                print(refPage_result)
                                                                        else:
                                                                                print(refInfo.text)
                                                                elif (refInfo.get('unit') == 'volume'):
                                                                        if (refInfo.text == None):

                                                                                refVolume_from = refInfo.get('from')
                                                                                refVolume_to = refInfo.get('to')
                                                                                refVolume_result = refVolume_from + ' ' + refVolume_to
                                                                                print(refVolume_result)

                                                                        else:
                                                                                print(refInfo.text)
                                                                elif (refInfo.get('unit') == 'issue'):
                                                                        if (refInfo.text == None):
                                                                                refIssue_from = refInfo.get('from')
                                                                                refIssue_to = refInfo.get('to')
                                                                                refIssue_result = refIssue_from + ' ' + refIssue_to
                                                                                print(refIssue_result)
                                                                        else:
                                                                                print(refInfo.text)
                                                        for refDate in imprint.findall(tag + 'date'):
                                                                refDate_year = refDate.get('when')
                                                                print(refDate_year)


                                                        #surname = persName.find(tag + 'surname').text

