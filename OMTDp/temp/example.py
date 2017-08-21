# example
# Created by JKChang
# 03/08/2017, 11:13
# Tag:
# Description: 

import xml.etree.ElementTree as ET
from Extractor import PMIDExtractor
from lxml import etree

stri = """
<responseWrapper>
<version>5.2.1</version>
<hitCount>1</hitCount>
<nextCursorMark>AoIIQOQbFigzNjg1NjUxNA==</nextCursorMark>
<request>
<query>EXT_ID:28644687</query>
<resultType>core</resultType>
<synonym>false</synonym>
<cursorMark>*</cursorMark>
<pageSize>25</pageSize>
<sort/>
</request>
<resultList>
<result>
<id>28644687</id>
<source>MED</source>
<pmid>28644687</pmid>
<doi>10.1080/15563650.2017.1334915</doi>
<title>
Massive paracetamol overdose: an observational study of the effect of activated charcoal and increased acetylcysteine dose (ATOM-2).
</title>
<authorString>
Chiew AL, Isbister GK, Kirby KA, Page CB, Chan BSH, Buckley NA.
</authorString>
<authorList>
<author>
<fullName>Chiew AL</fullName>
<firstName>Angela L</firstName>
<lastName>Chiew</lastName>
<initials>AL</initials>
<affiliation>
c New South Wales Poisons Information Centre , Children's Hospital at Westmead , Westmead , NSW , Australia.
</affiliation>
</author>
<author>
<fullName>Isbister GK</fullName>
<firstName>Geoffrey K</firstName>
<lastName>Isbister</lastName>
<initials>GK</initials>
<affiliation>
e Department of Clinical Toxicology and Pharmacology , Calvary Mater Newcastle , Newcastle , Australia.
</affiliation>
</author>
<author>
<fullName>Kirby KA</fullName>
<firstName>Katharine A</firstName>
<lastName>Kirby</lastName>
<initials>KA</initials>
<affiliation>
b Department of Pharmacology, School of Medical Sciences , University of Sydney , Sydney , NSW , Australia.
</affiliation>
</author>
<author>
<fullName>Page CB</fullName>
<firstName>Colin B</firstName>
<lastName>Page</lastName>
<initials>CB</initials>
<affiliation>
g Queensland Poisons Information Centre , Lady Cilento Children's Hospital , Brisbane , QLD , Australia.
</affiliation>
</author>
<author>
<fullName>Chan BSH</fullName>
<firstName>Betty S H</firstName>
<lastName>Chan</lastName>
<initials>BSH</initials>
<affiliation>
c New South Wales Poisons Information Centre , Children's Hospital at Westmead , Westmead , NSW , Australia.
</affiliation>
</author>
<author>
<fullName>Buckley NA</fullName>
<firstName>Nicholas A</firstName>
<lastName>Buckley</lastName>
<initials>NA</initials>
<authorId type="ORCID">0000-0002-6326-4711</authorId>
<affiliation>
c New South Wales Poisons Information Centre , Children's Hospital at Westmead , Westmead , NSW , Australia.
</affiliation>
</author>
</authorList>
<authorIdList>
<authorId type="ORCID">0000-0002-6326-4711</authorId>
</authorIdList>
<journalInfo>
<journalIssueId>2564942</journalIssueId>
<dateOfPublication>2017 Jun</dateOfPublication>
<monthOfPublication>6</monthOfPublication>
<yearOfPublication>2017</yearOfPublication>
<printPublicationDate>2017-06-01</printPublicationDate>
<journal>
<title>Clinical toxicology (Philadelphia, Pa.)</title>
<ISOAbbreviation>Clin Toxicol (Phila)</ISOAbbreviation>
<medlineAbbreviation>Clin Toxicol (Phila)</medlineAbbreviation>
<NLMid>101241654</NLMid>
<ISSN>1556-3650</ISSN>
<ESSN>1556-9519</ESSN>
</journal>
</journalInfo>
<pubYear>2017</pubYear>
<pageInfo>1-11</pageInfo>
<abstractText>
Paracetamol is commonly taken in overdose, with increasing concerns that those taking "massive" overdoses have higher rates of hepatotoxicity and may require higher doses of acetylcysteine. The objective was to describe the clinical characteristics and outcomes of "massive" (≥ 40 g) paracetamol overdoses.Patients were identified through the Australian Paracetamol Project, a prospective observational study through Poisons Information Centres in NSW and Queensland, over 3 and 1.5 years, respectively, and retrospectively from three clinical toxicology unit databases (over 2.5 to 20 years). Included were immediate-release paracetamol overdoses ≥ 40 g ingested over ≤ 8 h. Outcomes measured included paracetamol ratio[defined as the ratio of the first paracetamol concentration taken 4-16 h post-ingestion to the standard (150 mg/L at 4 h) nomogram line at that time] and hepatotoxicity (ALT >1000 U/L).Two hundred paracetamol overdoses were analysed, reported median dose ingested was 50 g (interquartile range (IQR): 45-60 g) and median paracetamol ratio 1.9 (IQR: 1.4-2.9, n = 173). One hundred and ninety-three received acetylcysteine at median time of 6.3 h (IQR: 4-9.3 h) post-ingestion. Twenty-eight (14%) developed hepatotoxicity, including six treated within 8 h of ingestion. Activated charcoal was administered to 49(25%), at median of 2 h post-ingestion (IQR:1.5-5 h). Those receiving activated charcoal (within 4 h of ingestion), had significantly lower paracetamol ratio versus those who did not: 1.4 (n = 33, IQR: 1.1-1.6) versus 2.2 (n = 140, IQR: 1.5-3.0) (p < .0001) (paracetamol concentration measured ≥ 1 h after charcoal). Furthermore, they had lower rates of hepatotoxicity [unadjusted OR: 0.12 (95% CI: <0.001-0.91); adjusted for time to acetylcysteine OR: 0.20 (95%CI: 0.002-1.74)]. Seventy-nine had a paracetamol ratio ≥2, 43 received an increased dose of acetylcysteine in the first 21 h; most commonly a double dose in the last bag (100 to 200 mg/kg/16 h). Those receiving increased acetylcysteine had a significant decrease risk of hepatotoxicity [OR:0.27 (95% CI: 0.08-0.94)]. The OR remained similar after adjustment for time to acetylcysteine and paracetamol ratio.Massive paracetamol overdose can result in hepatotoxicity despite early treatment. Paracetamol concentrations were markedly reduced in those receiving activated charcoal within 4 h. In those with high paracetamol concentrations, treatment with increased acetylcysteine dose within 21 h was associated with a significant reduction in hepatotoxicity.
</abstractText>
<affiliation>
c New South Wales Poisons Information Centre , Children's Hospital at Westmead , Westmead , NSW , Australia.
</affiliation>
<language>eng</language>
<pubModel>Print-Electronic</pubModel>
<pubTypeList>
<pubType>Journal Article</pubType>
</pubTypeList>
<keywordList>
<keyword>Activated charcoal</keyword>
<keyword>Hepatotoxicity</keyword>
<keyword>acetylcysteine</keyword>
<keyword>Overdose</keyword>
<keyword>paracetamol</keyword>
</keywordList>
<fullTextUrlList>
<fullTextUrl>
<availability>Subscription required</availability>
<availabilityCode>S</availabilityCode>
<documentStyle>doi</documentStyle>
<site>DOI</site>
<url>https://doi.org/10.1080/15563650.2017.1334915</url>
</fullTextUrl>
</fullTextUrlList>
<isOpenAccess>N</isOpenAccess>
<inEPMC>N</inEPMC>
<inPMC>N</inPMC>
<hasPDF>N</hasPDF>
<hasBook>N</hasBook>
<citedByCount>0</citedByCount>
<hasReferences>N</hasReferences>
<hasTextMinedTerms>N</hasTextMinedTerms>
<hasDbCrossReferences>N</hasDbCrossReferences>
<hasLabsLinks>Y</hasLabsLinks>
<authMan>N</authMan>
<epmcAuthMan>N</epmcAuthMan>
<nihAuthMan>N</nihAuthMan>
<hasTMAccessionNumbers>N</hasTMAccessionNumbers>
<dateOfCreation>2017-06-23</dateOfCreation>
<dateOfRevision>2017-06-23</dateOfRevision>
<electronicPublicationDate>2017-06-23</electronicPublicationDate>
<firstPublicationDate>2017-06-23</firstPublicationDate>
</result>
</resultList>
</responseWrapper>"""

root = ET.fromstring(stri)
for country in root.findall('result'):
    gdppc = country.find('title').text
    print(gdppc)