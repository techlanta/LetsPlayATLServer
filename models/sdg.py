from main import db

class SDG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    description = db.Column(db.String(1024))
    imageLink = db.Column(db.String(1024))

    def serialize(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "imageLink":self.imageLink,
        }

sdg_to_events = db.Table(
    "sdg_to_events",
    # db.Column("id", db.Integer, primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), nullable=False, primary_key=True),
    db.Column("sdg_id", db.Integer,  db.ForeignKey("SDG.id"), nullable=False, primary_key=True)
    )

ALL_SDG = [
    SDG(
        id=1,
        title="End poverty in all its forms everywhere",
        description="The decline of global extreme poverty continues, but has slowed. The deceleration indicates that the world is not on track to achieve the target of less than 3 per cent of the world living in extreme poverty by 2030. People who continue to live in extreme poverty face deep, entrenched deprivation often exacerbated by violent conflicts and vulnerability to disasters. Strong social protection systems and government spending on key services often help those left behind get back on their feet and escape poverty, but these services need to be brought to scale.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_60.jpg"
    ),
    SDG(
        id=2,
        title="End hunger, achieve food security and improved nutrition and promote sustainable agriculture",
        description="Hunger is on the rise again globally and undernutrition continues to affect millions of children. Public investment in agriculture globally is declining, smallscale food producers and family farmers require much greater support and increased investment in infrastructure and technology for sustainable agriculture is urgently needed.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_32.jpg"
    ),
    SDG(
        id=3,
        title="Ensure healthy lives and promote well-being for all at all ages",
        description="Major progress has been made in improving the health of millions of people, increasing life expectancy, reducing maternal and child mortality and fighting against leading communicable diseases. However, progress has stalled or is not happening fast enough with regard to addressing major diseases, such as malaria and tuberculosis, while at least half the global population does not have access to essential health services and many of those who do suffer undue financial hardship, potentially pushing them into extreme poverty. Concerted efforts are required to achieve universal health coverage and sustainable financing for health, to address the growing burden of non-communicable diseases, including mental health, and to tackle antimicrobial resistance and determinants of health such as air pollution and inadequate water and sanitation.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_68.jpg"
    ),
    SDG(
        id=4,
        title="Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
        description="Despite the considerable on education access and participation over the past years, 262 million children and youth aged 6 to 17 were still out of school in 2017, and more than half of children and adolescents are not meeting minimum proficiency standards in reading and mathematics. Rapid technological changes present opportunities and challenges, but the learning environment, the capacities of teachers and the quality of education have not kept pace. Refocused efforts are needed to improve learning outcomes for the full life cycle, especially for women, girls and marginalized people in vulnerable settings.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_16.jpg"
    ),
    SDG(
        id=5,
        title="Achieve gender equality and empower all women and girls",
        description="While some indicators of gender equality are progressing, such as a significant decline in the prevalence of female genital mutilation and early marriage, the overall idbers continue to be high. Moreover, insufficient progress on structural issues at the root of gender inequality, such as legal discrimination, unfair social norms and attitudes, decision-making on sexual and reproductive issues and low levels of political participation, are undermining the ability to achieve Sustainable Development Goal 5.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_44.jpg"
    ),
    SDG(
        id=6,
        title="Ensure availability and sustainable management of water and sanitation for all",
        description="Despite progress, billions of people still lack safe water, sanitation and handwashing facilities. Data suggests that achieving universal access to even basic sanitation service by 2030 would require doubling the current annual rate of progress. More efficient use and management of water are critical to addressing the growing demand for water, threats to water security and the increasing frequency and severity of droughts and floods resulting from climate change. As of the time of writing, most countries are unlikely to reach full implementation of integrated water resources management by 2030.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_28.jpg"
    ),
    SDG(
        id=7,
        title="Ensure access to affordable, reliable, sustainable and modern energy for all",
        description="Access to electricity in the poorest countries has begun to accelerate, energy efficiency continues to improve and renewable energy is making gains in electricity sector. Despite this progress, some 800 million people remain without electricity while access to clean cooking fuels and technologies needs dedicated attention. In addition, if Sustainable Development Goals 7, 13 and related Goals are to be met, much higher levels of ambition are required with regard to renewable energy, including transportation and heating.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_8.jpg"
    ),
    SDG(
        id=8,
        title="Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
        description="Inclusive and sustainable economic growth can drive progress and generate the means to implement the Sustainable Development Goals. Globally, labour productivity has increased and unemployment is back to pre-financial crisis levels. However, the global economy is growing at a slower rate. More progress is needed to increase employment opportunities, particularly for young people, reduce informal employment and the gender pay gap and promote safe and secure working environments to create decent work for all.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_20.jpg"
    ),
    SDG(
        id=9,
        title="Ensure healthy lives and promote well-being for all at all ages",
        description="Aspects of the prevailing global economic environment have not been conducive to rapid progress on Sustainable Development Goal 9. While financing for economic infrastructure has increased in developing countries and impressive progress has been made in mobile connectivity, countries that are lagging behind, such as least developed countries, face serious challenges in doubling the manufacturing industry’s share of GDP by 2030, and investment in scientific research and innovation remains below the global average.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_12.jpg"
    ),
    SDG(
        id=10,
        title="Reduce inequality within and among countries",
        description="Inequality within and among nations continues to be a significant concern despite progress in and efforts at narrowing disparities of opportunity, income and power. Income inequality continues to rise in many parts of the world, even as the bottom 40 per cent of the population in many countries has experienced positive growth rates. Greater emphasis will need to be placed on reducing inequalities in income as well as those based on other factors. Additional efforts are needed to increase zero-tariff access for exports from least developed countries and developing countries, and assistance to least developed countries and small island developing States.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_36.jpg"
    ),
    SDG(
        id=11,
        title="Make cities and human settlements inclusive, safe, resilient and sustainable",
        description="Substantial progress has been made in reducing the proportion of the global urban population living in slums, though more than 1 billion people continue to live in such situations. Urgent action is needed to reverse the current situation, which sees the vast majority of urban residents breathing poor-quality air and having limited access to transport and open public spaces. With the areas occupied by cities growing faster than their populations, there are profound repercussions for sustainability.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_40.jpg"
    ),
    SDG(
        id=12,
        title="Ensure sustainable consumption and production patterns",
        description="Worldwide material consumption has expanded rapidly, as has material footprint per capita, seriously jeopardizing the achievement of Sustainable Development Goal 12 and the Goals more broadly. Urgent action is needed to ensure that current material needs do not lead to the overextraction of resources or to the degradation of environmental resources, and should include policies that improve resource efficiency, reduce waste and mainstream sustainability practices across all sectors of the economy.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_64.jpg"
    ),
    SDG(
        id=13,
        title="Take urgent action to combat climate change and its impacts",
        description="With rising greenhouse gas emissions, climate change is occurring at rates much faster than anticipated and its effects are clearly felt worldwide. While there are positive steps in terms of the climate finance flows and the development of nationally determined contributions, far more ambitious plans and accelerated action are needed on mitigation and adaptation. Access to finance and strengthened capacities need to be scaled up at a much faster rate, particularly for least developed countries and small island developing States.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_72.jpg"
    ),
    SDG(
        id=14,
        title="Conserve and sustainably use the oceans, seas and marine resources for sustainable development",
        description="The expansion of protected areas for marine biodiversity and existing policies and treaties that encourage responsible use of ocean resources are still insufficient to combat the adverse effects of overfishing, growing ocean acidification due to climate change and worsening coastal eutrophication. As billions of people depend on oceans for their livelihood and food source and on the transboundary nature of oceans, increased efforts and interventions are needed to conserve and sustainably use ocean resources at all levels.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_76.jpg"
    ),
    SDG(
        id=15,
        title="Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss",
        description="There are some encouraging global trends in protecting terrestrial ecosystems and biodiversity. Forest loss is slowing down, more key biodiversity areas are protected and more financial assistance is flowing towards biodiversity protection. Yet, the 2020 targets of Sustainable Development Goal 15 are unlikely to be met, land degradation continues, biodiversity loss is occurring at an alarming rate, and invasive species and the illicit poaching and trafficking of wildlife continue to thwart efforts to protect and restore vital ecosystems and species.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_4.jpg"
    ),
    SDG(
        id=16,
        title="Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels",
        description="Advances in ending violence, promoting the rule of law, strengthening institutions and increasing access to justice are uneven and continue to deprive millions of their security, rights and opportunities and undermine the delivery of public services and broader economic development. Attacks on civil society are also holding back development progress. Renewed efforts are essential to move towards the achievement of Sustainable Development Goal 16.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_48.jpg"
    ),
    SDG(
        id=17,
        title="Strengthen the means of implementation and revitalize the global partnership for sustainable development",
        description="Progress on some means of implementation targets is moving rapidly: personal remittances are at an all-time high, an increasing proportion of the global population has access to the Internet and the Technology Bank for the Least Developed Countries has been established. Yet, significant challenges remain: ODA is declining, private investment flows are not well aligned with sustainable development, there continues to be a significant digital divide and there are ongoing trade tensions. Enhanced international cooperation is needed to ensure that sufficient means of implementation exist to provide countries the opportunity to achieve the Sustainable Development Goals.",
        imageLink="https://sustainabledevelopment.un.org/content/images/image_logo_clean10008_56.jpg"
    ),

]

def get_sdg(id):
    if id < 1 or id > 17:
        return "invalid input"
    else:
        sdg = SDG.query.filter_by(id=id).first()
        return sdg.serialize()
