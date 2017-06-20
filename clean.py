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


title_result = ''
abstract_result = ''
date_result = ''
venue_result = ''
page_result = ''
volume_result = ''
number_result = ''
ncite = 0
version_result = ''
version_time_result = ''

for child in root:
        for lower in child:
                #print(lower.tag)
                #find name
                try:
                        for titleStmt in lower.findall(tag + 'titleStmt'):
                                        #print(titleStmt.tag)
                                title_result = titleStmt.find(tag + 'title').text
                                #print(title_result)
                except:
                        title_result = ''


        for abstract_parent in child:
                #find abstract
                try:
                        for abstract_elem in abstract_parent.findall(tag + 'abstract'):
                                abstract_result = abstract_elem.find(tag + 'p').text

                        #print(abstract_result)

                except:
                        abstract_result = ''
        for publication_date in child:
                #find publication date

                try:
                        for publicationStmt in publication_date.findall(tag + 'publicationStmt'):
                                date_tag = publicationStmt.find(tag + 'date')
                                date_result = date_tag.text
                        #print(date_result)
                except:
                        date_result = ''
        for version_parent in child:
                #find version name

                try:
                        for version_child in version_parent.findall(tag + 'appInfo'):
                                for version in version_child:

                                        version_result = version.get('ident')

                #find versionTime
                                        version_time_result = version.get('when')
                                #print(version_time_result)
                except:
                        version_result = ''
                        version_time_result = ''

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
                                                                print(' '.join(name_result))
                                                        except:
                                                                print()
                                                        #get affiliation
                                                        for affiliation in author.findall(tag + 'affiliation'):
                                                                try:
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
                                                                except:
                                                                        print()
                                                        #get email
                                                        try:
                                                                for email in author.findall(tag + 'email'):
                                                                        print(email.text)
                                                        except:
                                                                print('Null')
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
                                                                number_result = issue_result

ncite = 0
for teiHeader in root:

        for front in teiHeader:
                for div in front:
                        for listBibl in div:
                                for biblStruc in listBibl:
                                        for analytic in biblStruc.findall(tag + 'analytic'):
                                                finalarray = []
                                                for title in analytic.findall(tag + 'title'):
                                                        finalarray.append(title.text)

                                                for title in analytic.findall(tag + 'author'):

                                                        for persName in title:
                                                                refName_result = []
                                                                for refName in persName.getchildren():

                                                                        refName_result.append(refName.text)


                                                                print((', '.join(refName_result)))
                                                        #print(finalarray)
                                        for monogr in biblStruc.findall(tag + 'monogr'):
                                                for imprint in monogr:
                                                        try:

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
                                                        except:
                                                                print('1')
                                        ncite = ncite + 1
venue_result = 'Null'



if (title_result == ''):
        title_result = 'Null'
if (abstract_result == ''):
        abstract_result = 'Null'
if (date_result == ''):
        date_result = 'Null'
if (page_result == ''):
        page_result = 'Null'
if (volume_result == ''):
        volume_result = 'Null'
if (number_result == ''):
        number_result = 'Null'
if (version_result == ''):
        version_result = 'Null'
if (version_time_result == ''):
        version_time_result = 'Null'

venue_result = 'Null'
result_array = []
result_array.extend([basetag, title_result, abstract_result, date_result, venue_result, page_result, volume_result, number_result, version_result, version_time_result])
#print(result_array)
                                                        #surname = persName.find(tag + 'surname').text
                                                        #something.append(firstname)
                                                        #print(something)
                                                        #forme.get('type') middlename in persName:
