import streamlit as st
from utils.helpers import save_prompt, load_prompts
import pyperclip

# 自定义CSS样式
def load_css():
    st.markdown("""
    <style>
        /* 主题颜色 */
        :root {
            --primary-color: #1f77b4;
            --background-color: #f0f2f6;
            --secondary-background-color: #ffffff;
            --text-color: #31333F;
        }
        
        /* 标题样式 */
        .main-title {
            color: #1f77b4;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            padding: 1rem;
            border-bottom: 2px solid #1f77b4;
        }
        
        /* 分类标题样式 */
        .category-title {
            color: #2c3e50;
            font-size: 1.2rem;
            font-weight: 600;
            margin: 1rem 0;
            padding: 0.5rem;
            background-color: #f8f9fa;
            border-radius: 5px;
        }
        
        /* 按钮样式 */
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            margin: 0.2rem 0;
            background-color: #ffffff;
            border: 1px solid #1f77b4;
            color: #1f77b4;
            transition: all 0.3s;
        }
        
        .stButton>button:hover {
            background-color: #1f77b4;
            color: #ffffff;
        }
        
        /* 文本区域样式 */
        .stTextArea>div>div>textarea {
            border-radius: 5px;
            border: 1px solid #e0e0e0;
            padding: 1rem;
            font-size: 1rem;
            line-height: 1.5;
        }
        
        /* 分隔线样式 */
        hr {
            margin: 2rem 0;
            border: none;
            height: 1px;
            background-color: #e0e0e0;
        }
        
        /* 卡片样式 */
        .css-12w0qpk {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        }
        
        /* 提示词详情区域样式 */
        .prompt-detail {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        }
    </style>
    """, unsafe_allow_html=True)

def get_prompts_content():
    """返回所有提示词的内容"""
    return {
        # 一、学术角色预设
        "学术角色": {
            "title": "学术角色",
            "content": """As a leader in the academic field, I possess extensive academic experience and professional knowledge across various domains. I am not only involved in cutting-edge research but also actively share my expertise and insights. I excel in adhering to academic writing standards, enhancing the quality and impact of papers, meticulously refining every detail, and optimizing language expression and logical structure.
我作为学术领域的引领者，在各个领域拥有丰富的学术经验与专业知识，不仅参与前沿研究，还积极分享经验与见解擅长学术写作规范，提升论文的品质与影响力，精细润色每个细节，优化语言表达与逻辑结构"""
        },
        "论文评审专家": {
            "title": "论文评审专家",
            "content": """You are now acting as an expert in the field of [Put professional fields here…]. From a professional point of view, do you think there is any need to modify the above content? Be careful not to modify the whole text, you need to point out the places that need to be modified one by one, and give revision opinions and recommended revision content.
你现在扮演一个[这里放你所研究的领域] 领域的专家，从专业的角度，您认为上面些内容是否有需要修改的地方？注意，不要全文修改，您需要一一指出需要修改的地方，并且给出修改意见以及推荐的修改内容"""
        },
        
        # 二、论文撰写指令
        "写标题": {
            "title": "写标题",
            "content": """I will provide you with the abstract and key words of a scientific paper in any language and you will detect the language and reply in the same language. Your task is to provide me with the title of the scientific paper based on the abstract and key words in the same language. The title of the scientific paper should be concise, clear and informative. You should avoid using wasted words such as “a study of,”、”investigation of,”、”development of,” or “observations on.” Make sure the title can grip the audience immediately. My abstract is “XXX”, my key words are “XXX”
我将向你提供一篇任何语言的科学论文的摘要和关键词，你将检测该语言并以相同的语言进行回复。你的任务是根据摘要和关键词用相同的语言向我提供科学论文的标题。科学论文的标题应该是简洁、明确和有信息量的。你应该避免使用诸如研究、调查、发展或观察等词语。确保标题能够立即抓住听众的心。"""
        },
        "写英文标题": {
            "title": "写英文标题",
            "content": """I want you to act as an academic journal editor. I am going to provide you an abstract of manuscript and you provide me with 5 good titles in English for a research paper and give explanation for why this title is good. Provide your output as a markdown table with two columns and with head in Chinese. First column gives titles in English and second column provides explanation in Chinese. 
希望你担任一名学术期刊编辑。我将为你提供一个手稿的摘要，你需要为一篇研究论文提供5个好的英文标题，并解释为什么这个标题好。请以Markdown表格的形式提供你的输出，表格有两列，标题用中文。第一列给出英文标题，第二列用中文提供解释。"""
        },
        "写摘要": {
            "title": "写摘要",
            "content": """Act as an academic research expert. Draft an abstract for a research paper titled [title]. The abstract should succinctly summarize the main objectives, methodologies, key findings, and implications of the research.
作为学术研究专家，为研究论文撰写一个简洁、精确的摘要。"""
        },
        "写英文摘要": {
            "title": "写英文摘要",
            "content": """Please read through the uploaded manuscript and write an abstract in English for it. The abstract should initiate with a comprehensive summary of the broader context or background of the study, followed by a statement that describe the gaps, limitations or issues. Then, describe the research methods used in the manuscript. After that, write 3-5 sentences showing the key findings. In the end, include a statement which underscores the unique value or significant contribution of the manuscript. After generating the abstract, give explanation in Chinese checking if you have followed the instruction in a markdown table.
请阅读上传的手稿，并为其撰写一份英文摘要。摘要应首先提供研究背景或更广泛背景的全面概述，接着陈述描述研究的空白、局限性或问题。然后，描述手稿中使用的研究方法。此后，写出3-5句话展示关键发现。最后，包括一份强调手稿独特价值或重大贡献的声明。在生成摘要后，以中文提供解释，检查你是否遵循了指令，并以Markdown表格形式展示。"""
        },
        "缩写名称": {
            "title": "缩写名称",
            "content": """What abbreviations can “XXX” have? Give several options, with reasons, for use in an academic paper. “XXX”
可以有哪些缩写？请给出几���选择，并给出理由，以便用于论文中。"""
        },
        "论文续写": {
            "title": "论文续写",
            "content": """Based on the knowledge you have mastered about [xxx], polish and continue writing the above content to make the content richer and more complete.
根据你所掌握的关于[xxx]的知识，润色并续写上面的内容，使得内容更加丰富完整。"""
        },
        "论文致谢": {
            "title": "论文致谢",
            "content": """我想请你帮我写一份关于我的论文的致谢。我的论文的题目是(题目)，我的导师是(导师)，我的合作者是(合作者)。我想感谢以下的人或机构：
(感谢对象1):感谢他们对我的(帮助或贡献)
(感谢对象2):感谢他们对我的(帮助或贡献)
(感谢对象n):感谢他们对我的(帮助或贡献)
你能根据这些信息，写一份大约(字数)字的致谢吗?请使用礼貌和诚恳的语气并注意格式和标点。"""
        },
        "论文大纲": {
            "title": "论文大纲",
            "content": """Act as an academic research expert. Draft a comprehensive research paper outline on [topic]. The outline should be well-structured, starting with a compelling introduction that states the problem or question, the relevance of the topic, and the objectives of the research.
作为学术研究专家，为研究论文起草一个结构良好的大纲，明确研究的主要部分。"""
        },
        
        # 三、学术润色指令
        "英文润色1": {
            "title": "英文润色1",
            "content": """The following is a paragraph from a n academic paper. Refinish writing to conform to academic style，improve spelling，grammar，clarity, conciseness and overall readability. If necessary, rewrite the entire sentence. In addition,list all modifications in the Markdown table and explain the reasons for doing so.Paragraph ：（+the paragraph that requires polishing）
以下是一篇学术论文中的一段文字。请重新润色写作，以符合学术风格，提高拼写、语法、清晰度、简洁性和整体可读性。如有必要，重写整个句子。此外，请在Markdown表格中列出所有修改，并解释修改的原因。段落：（+润色内容）。"""
        },
        "英文润色2": {
            "title": "英文润色2",
            "content": """Below is a paragraph from an academic paper. Polish the writing to meet the academic style,improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. Furthermore, list all modification and explain the reasons to do so in markdown table. Paragraph ：XXX
以下是一篇学术论文中的段落。请润色写作以符合学术风格，提高拼写、语法、清晰度、简洁性和整体可读性。如有必要，重写整个句子。此外，请在Markdown表格中列出所有修改，并解释修改的原因。段落：XXX"""
        },
        "中文润色": {
            "title": "中文润色",
            "content": """As a Chinese academic paper writing improvement assistant, your task is to enhance the spelling, grammar, clarity, conciseness, and overall readability of the provided text. Break down long sentences, reduce repetition, and offer suggestions for improvement. Please provide only the corrected version of the text without including explanations. Edit the following text: (content to be polished)
作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本：（润色内容）"""
        },
        "SCI论文润色": {
            "title": "SCI论文润色",
            "content": """I am preparing my SCI paper for submission and require assistance in polishing each paragraph. Could you please refine my writing for academic rigor? I need you to correct any grammatical errors, improve sentence structure for academic suitability, and make the text more formal where necessary. For each paragraph we need to improve, you need to put all modified sentences in a Markdown table, each column contains the following: Full original sentence; Highlight the revised part of the sentence; Explain why made these changes. Finally, Rewrite the full, corrected paragraph. If you understand, please reply: yes, let’s get started.
我正在准备我的SCI论文以便提交，需要帮助润色每段落。你能帮我提升学术严谨性吗？我需要你纠正任何语法错误，改进句子结构以适应学术要求，并在必要时使文本更加正式。对于每个需要改进的段落，你需要将所有修改后的句子放在一个Markdown表格中，每一列分别包含以下内容：完整的原始句子；突出显示句子的修订部分；解释为什么做出这些更改。最后，重写整个更正后的段落。如果你理解了，请回复：是的，让我们开始吧。"""
        },
        "期刊会议风格": {
            "title": "期刊会议风格",
            "content": """If I wish to publish a paper at a XXX conference, please polish the above content in the style of a XXX article.
提示：如果我希望将论文发表在XXX会议/期刊上，请按照XXX文章的风格，对上面的内容进行润色。"""
        },
        "润色英文段落结构和句子逻辑": {
            "title": "润色英文段落结构和句子逻辑",
            "content": """I am a researcher studying +（你的研究方向） and now trying to revise my manuscript which willbe subrnitted to the +（你的投稿期刊）. want you to analyze the logic and coherence amongsentences within each paragraph in the following text, ldentify any areas where the flow orconnections between sentences could be improved,and provide specific suagestions toenhance the overall quality and readabllity to the content. Please only provide the text aftelimproving and then give a list of the improvements in Chinese. lf you understand the abovetask, please reply with yes, and then I will provide you with the text.
        
我是一名研究人员，研究方向是 +（你的研究方向），目前正在尝试修改我的手稿，该手稿将提交到 +（你的投稿期刊）。我希望你分析每段文字中的逻辑性和连贯性，识别出句子之间的衔接部分是否有待改善，并提供具体的建议，以提升内容的整体质量和可读性。请仅提供修改后的文本，并给出改进的中文列表。如果你理解上述任务，请回复“是的”，然后我会提供文本。"""
        },
        "直接润色段落": {
            "title": "直接润色段落",
            "content": """Polish the paragraph above to make it more logical, and academic.
润色上面的内容，使其更加更合逻辑，更符合学术风格。"""
        },
        "多版本参考": {
            "title": "多版本参考",
            "content": """Please provide multiple versions for reference
这里给出了其它两版的参考，方便我们参考对比"""
        },
        "错误纠正": {
            "title": "错误纠正",
            "content": """如果ChatGPT理解错了你的问题，可以给它一个错误的反馈，让它重新回答

Prompt: Note that it is not ….., but ….. Re-answer the previous question based on what I have added.
注意，不是…而是… 请根据我的补充，重新回答上个问题"""
        },
        "重新回答": {
            "title": "重新回答",
            "content": """如果认为回答的不够好，或者方向不对。可以要求重新回答，并且指明侧重方向。比如你只希望去除当前段落的冗余，并不想改动原意思。

Still the above question, I think your answer is not good enough. Please answer again, this time focusing on removing redundancy from this passage.
还是上面的问题，我认为你回答的不够好。请重新回答一次，这次你应该侧重于去除这段话中的冗余。"""
        },
        "语法检查/查找语法错误": {
            "title": "语法检查/查找语法错误",
            "content": """Can you help me ensure that the grammar and the spelling is correct? Do not try to polish the text, if no mistake is found, tell me that this paragraph is good. If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, put the original text the first column, put the corrected text in the second column and highlight the key words you fixed. Example: Paragraph: How is you? Do you knows what is it? | Original sentence | Corrected sentence | | :— | :— | | How is you? | How are you? | | Do you knows what is it? | Do you know what it is? | Below is a paragraph from an academic paper. You need to report all grammar and spelling mistakes as the example before. Paragraph: XXX
你能帮助我确保语法和拼写正确无误吗？不要尝试润色文本，如果没有发现错误，请告诉我这段话很好。如果你发现了语法或拼写错误，请按照之前的例子，在双列的Markdown表格中列出你发现的错误，第一列放原始文本，第二列放更正后的文本，并突出显示你修正的关键词。示例：| 原始句子 | 更正后的句子 | | :— | :— | | How is you? | How are you? | | Do you knows what is it? | Do you know what it is? |
以下是一篇学术论文中的段落。你需要按照上述例子报告所有语法和拼写错误。段落：XXX"""
        },
        "语法校正": {
            "title": "语法校正",
            "content": """I am a researcher studying +（你的研究方向） and now trying to revise my manuscript which willbe submitted to the +（你的投稿期刊）. Please help me to ensure the grammar and spellingare correct. Do not try to improve the text, if no mistake found, tell me this paragraph is good.If you find grammar or spelling mistakes, please list the mistakes you find in a two-columnmark down table, put the original text in the first column, put the corrected text in the second column, and do highlight the key words you fixed in bold."""
        },
        "语法句法": {
            "title": "语法句法",
            "content": """
This sentence is grammatically incorrect. Please revise.
这句话在语法上是不正确的。请修改。
The subject and verb do not agree in this sentence. Please correct.
主语和动词在这句话中不一致。请改正。
This phrase seems out of place. Please rephrase to improve clarity.
这句话似乎不合适。请重新措辞以表达更清晰。
I have used a passive voice in this sentence. Consider using an active voice instead.
我在这句话中使用了被动语态。考虑改用主动语态。"""
        },
        "润色定位": {
            "title": "润色定位",
            "content": """Note that in addition to giving the modified content, please also indicate which paragraphs and sentences have been modified in the revised version.
注意，除了给出润色修改之后的内容，还请指明修订的本中具体修改了哪些段落的哪几句话。"""
        },
        "修改建议": {
            "title": "修改建议",
            "content": """You are now acting as an expert in the field of lung cancer From a professional point of view, do you think there is any need to modify the above content? Be careful not to modify the whole text, you need to point out the places that need to be modified one by one, and give revision opinions and recommended revision content.
你现在扮演一个[这里放你所研究的领域] 领域的专家，从专业的角度，您认为上面这些内容是否有需要修改的地方？注意，不要全文修改，您需要一一指出需要修改的地方，并且给出修改意见以及推荐的修改内容。"""
        },
        "修改意见": {
            "title": "修改意见",
            "content": """I started to write an academic paper, the title is XXXXX, now I have finished the introduction part, but I am not sure whether it is suitable, can you help me to read it, and put forward detailed and specific revision suggestions?
我开始写论文了，题目是XXXXX，现在我完成了引言部分，但是不确定是否合适，你能帮我看一下，并提出详细具体的修改意见吗？"""
        },
        "封装基本事实/原理/背景": {
            "title": "封装���本事实/原理/背景",
            "content": """润色的同时，修改基本逻辑错误。如果对内容的润色需要一些背景知识，可以在对话时主动告诉ChatGPT，比如XXX原理。

Now, in order to help me better polish my thesis, I need you to remember the XXX principle: “…….”
现在，为了接下来能够帮我更好的润色论文，我需要你记住XXX原理：“…….”

这样就相当于为一段内容，封装了一个函数名称，之后你再次提到XXX原理的时候，ChatGPT就能快速知道你说的是哪些基本事实了。

Polish and rewrite the above content to make it more in line with the style of academic papers, and at the same time, it can be more professional. If there are parts that do not conform to facts or logic, please refer to the part of xxxxx for the above content modification.
润色并重写上面的内容，使其更加符合论文的风格，于此同时，又能更加专业化，如果有不符合事实或者逻辑的部分，请你参考XXX原理部分对上面的内容修改。"""
        },
        "逻辑论证辅助": {
            "title": "逻辑论证辅助",
            "content": """Please help me analyze and optimize the logical structure of this argument to make it more convincing.
请帮我分析优化这段论证的逻辑结构，以使其更具说服力。"""
        },
        "个性化润色": {
            "title": "个性化润色",
            "content": """
更精确的术语(More precise)：选择更精确的词汇，例如使用“generate”代替“produce”
精炼表达(More concise)：去除冗余的表达以提高句子的清晰度和直接性。
客观的语言(More objective)：剔除含糊和主观性表述，以客观方式呈现信息。
细化描述(More specific)：提供更具体的细节，以支持论点或想法。
更连贯的表达(More coherent)：确保句子的组织性良好，逻辑流畅。
保持风格一致(More consistent)：确保用词和语调与整篇论文保持一致。
符合学术风格(More academic)：运用正确的学术用语如“moreover”和“consequently”。
规范语法(More formal grammar)：使用正确的语法或句法，避免语句不完整或偏离主题。
深化细节描绘(More nuanced)：使用精准的词汇和短语描述复杂或微妙的概念，使句子更加细化。
Make nuanced adjustments:对文本进行微调
lmplement marginal modifications:进行边际性修改
Clarify through rewording:改述以增强清晰性
Streamline sentence composition:简化句子结构
Verify grammatical correctness and orthography:校验语法��拼写正确性
lmprove textual fluidity and consistency:提升文本的流畅度和连贯性
Refine diction：措辞精练
Adjust for stylistic alignment：调整风格
Execute substantial revisions：执行重要的编辑
Overhaul content framework:改变内容架构"""
        },
        
        # 四、中英翻译指令
        "论文翻译": {
            "title": "论文翻译",
            "content": """I would like you to serve as an English translator, proofreader, and editor to translate my upcoming Chinese content into elegant, refined, and academic English. Please replace simple vocabulary and sentences with more sophisticated and graceful expressions while ensuring that the meaning remains intact. Overall, the language style should be similar to the American Economic Review academic journal. If you understand, please provide an example first.
我希望您能担任我的英文翻译、校对和编辑工作，将我即将推出的中文内容翻译成优雅、精炼且具有学术性的英文。请在保持原意不变的前提下，将简单的词汇和句子替换为更复杂、更优美的表达方式。总体而言，语言风格应类似于《美国经济评论》学术期刊。如果您理解了，请先提供一个示例。"""
        },
        "中译英1": {
            "title": "中译英1",
            "content": """Please translate following sentence to English:XXX
请将以下句子翻译成中文：XXX"""
        },
        "中译英2": {
            "title": "中译英2",
            "content": """Translate the above Chinese into the corresponding English, requiring the writing style of an academic paper
将上面的中文，翻译成对应的英语，要求具有论文的写作风格"""
        },
        "中译英3": {
            "title": "中译英3",
            "content": """I am a researcher studying +（Your research direction） and now trying to revise my manuscript which willbe submitted to the+（Your submission journal）. I want you to act as a scentiic English-Chnesetranslator,I will provide you with some paragraphs in one language and your task is toaccurately and academically translate the paragraphs only into the other language. I want you to give the output in a markdown table where the first colurrn is the onginal language andthe second is the first version of translation and third column is the second version of thetranslation, and give each row only one sentence. lf you understand the above task, pleasereply with yes, and then l will provide you with the paragraphs.
我是一名研究者，专注于+（你的研究方向），目前正在修订我的��稿，准备提交至+（你的投稿期刊）。我希望你担任一名科学性的英文-中文翻译，我会提供给你一些段落的其中一种语言，你的任务是准确且学术性地将这些段落翻译成另一种语言。我希望你以Markdown表格的形式给出翻译结果，其中第一列是原文，第二列是第一版的翻译，第三列是第二版的翻译，并且每行只包含一句翻译。如果你理解了上述任务，请回复“是的”，然后我会提供给你这些段落。"""
        },
        "中英互译": {
            "title": "中英互译",
            "content": """I want you to act as a scientific English-Chinese translator, I will provide you with some paragraphs in one language and your task is to accurately and academically translate the paragraphs only into the other language. Do not repeat the original provided paragraphs after translation. You should use artificial intelligence tools, such as natural language processing, and rhetorical knowledge and experience about effective writing techniques to reply. I’ll give you my paragraphs as follows, tell me what language it is written in, and then translate:XXX
我希望你担任一名科学性的英文-中文翻译员，我会提供一些段落给你，你的任务是准确且学术性地将这些段落翻译成另一种语言��翻译后请不要重复文段落。你应该使用人工智能工具，比如自然语言处理，以及关于有效写作技巧的修辞知识和经验来进行回复。我将如下提供我的段落，告诉我它是用什么语言写的，然后进行翻译：XXX"""
        },
        
        # 五、论文查重降重指令
        "内容降重": {
            "title": "内容降重",
            "content": """I would like you to act as an expert in the [field of your choice], and help students with plagiarism check for their papers. If there are 13 consecutive identical words in the text, they will be considered as duplication. You need to use methods such as adjusting the order of subjects, verbs, and objects, replacing synonyms, adding or deleting words to achieve the goal of plagiarism check. Please modify the following paragraph:

我想让你充当一位[你希望的某个]领域的专家，帮助学生进行论文的去重修改。如果文章中连续13个字一样，就算重复。你需要通过调整主谓宾语序替换同义词、增减字数等方法，来达到论文去重的目的。请你修改下面这段文字：
"""
        },
        "改写降重": {
            "title": "改写降重",
            "content": """Please rephrase this passage by adjusting the word order, modifying the length, and substituting synonyms to avoid any sequence of eight consecutive words that match the original text, ensuring that the revised content is more logical and adheres to academic standards.

请将这段话改写，通过调整语序增减字数，替换同义词等方式，避免与原文出现连续八个字相同的句子，使这段话更加有逻辑，符合论文的规范。
"""
        },
        "同义词替换降重": {
            "title": "同义词替换降重",
            "content": """Please assist me in reorganizing the following sentence by adjusting its logical structure, employing active and passive voice interchange, synonym replacement, and paraphrasing with near-synonyms to rewrite the sentence. Additionally, break down complex sentences and reduce repetition. Provide only the corrected version of the text.

请帮我把下面句子重新组织，通过调整句子逻辑，利用主动被动替换，同义词替换，近义词替换来改写句子，同时分解长句，减少重复，请只提供文本的更正版本。
"""
        },
        "避免连续相同": {
            "title": "避免连续相同",
            "content": """Please reduce the repetition in the following content by adjusting the order of words, modifying the length, and substituting synonyms to avoid any sequence of eight consecutive words that match the original text, ensuring that the passage is more logical and adheres to the standards of academic writing.

请将下面的内容降低重复率，通过调整语序增减字数，替换同义词等方式，避免与原文出现连续8个字相同的句子，使这段话更加具有逻辑，符合论文的规范。
"""
        },
        "缩写扩写降重": {
            "title": "缩写扩写降重",
            "content": """Please rewrite this passage by adjusting the order of words, increasing or decreasing the number of words, and substituting synonyms to avoid any sequence of three consecutive words that match the original text. Ensure that the revised passage is more logical and adheres to the standards of academic writing. Then, expand upon the content. Finally, condense it to fit the style of an academic paper.

请将这段话改写，通过调整语序增减字数，替换同义词等方式，避免与原文出现连续三个字相同的句子，使这段话更加有逻辑，符合论文的规范。然后再进行扩写。最后再缩写，符合论文风格。
"""
        },
        "关键词汇替换降重": {
            "title": "关键词汇替换降重",
            "content": """Kindly replace key terms in this section with appropriate synonyms to reduce similarity and enhance originality without compromising the meaning or academic integrity.

请替换本节中的关键词汇为合适的同义词，以降低相似度并增强原创性，同时不影响意义或学术完整性。
"""
        },
        "句式变换降重": {
            "title": "句式变换降重",
            "content": """Rewrite the sentences in this paragraph by changing the grammatical constructions and incorporating alternative expressions to avoid any sequence of five consecutive words that are identical to the original.

请通过改变句法结构和加入替代表达方式，重写本段中的句子，避免出现连续五个字与原文完全相同的情况。
"""
        },
        "逻辑重组": {
            "title": "逻辑重组",
            "content": """Reorganize the logic of this argument by restructuring sentences and paragraphs, ensuring that the flow of ideas is coherent and distinct from the original text.

请通过重构句子和段落的逻辑，确保思想的流畅性并且与原文有所区别。
"""
        },
        "综合改写": {
            "title": "综合改写",
            "content": """Revise this section by integrating new ideas and perspectives, rephrasing to ensure that the content is unique and adheres to academic standards of citation and originality.

请通过整合新的想法和视角来修改本节，重新表述以确保内容具有独特性，并符合学术引用和原创性的标准。
"""
        },
        "概念解释降重": {
            "title": "概念解释降重",
            "content": """Explain the concepts in your own words after understanding their meaning, to reduce the reliance on the original text and increase the level of original thought.

请在理解其含义后用自己的话解释概念，以减少对原文的依赖并提高原创思考的水平。
"""
        },
        
        # 六、参考文献指令
        "检查参考文献格式": {
            "title": "检查参考文献格式",
            "content": """I’d like you to serve as a reference editor for a research manuscript. I will supply you with five reference templates that you should use as guidelines. Following that, I will provide additional references for which you’ll need to examine formatting aspects such as punctuation placement and spacing. It is essential that the provided references align cohesively with the five initial templates. Provide me with any necessary corrections or suggestions for improve the text. Give a markdown table with three columns where the first is the original text, second is the fixed text, explanation in the third column, and then provide all fixed references. Below are the five example templates and references needed to be fixed:
我希望您能担任一篇研究手稿的参考文献编辑。我将为您提供五个参考文献模板，您应该将其作为指导方针使用。之后，我将提供额外的参考文献，您需要检查诸如标点符号位置和间距等格式方面的问题。所提供的参考文献必须与最初的五个模板保持一致性。请向我提供任何必要的更正建议或改进文本的建议。请提供一个Markdown表格，表格有三列，第一列是原文，第二列是更正后的文本，第三列是解释，然后提供所有已更正的参考文献。以下是五个示例模板和需要更正的参考文献："""
        },
        "APA格式校正": {
            "title": "APA格式校正",
            "content": """Please first correct the following reference format according to APA style, adjusting it to strictly comply with APA citation format. Finally, I need the references to be displayed in a Markdown format code block. It is important to note that the journal names should be in full and italicized (additional requirements can be added here). Here are my references:
首先请按照 APA 格式对以下参考文献格式进行校正，调整为严格符合 APA 的文献格式，最后我需要将参考文献以 Markdown 格式的代码块形式展示。需要注意的是期刊名称要全称，且斜体(这里可以添加其他要求)，下面是我的参考文献："""
        },
        
        # 七、投稿审稿指令
        "撰写Cover letter": {
            "title": "撰写Cover letter",
            "content": """I want you to act as an academic journal editor. I will provide you with the title and abstract of my manuscript. You need to write a format cover letter for submitting the manuscript to the Nature journal. You should state that the manuscript did not consider for publication in any other journal. Briefly introduce the merit of the manuscript and provide a short summary to point out the importance of the results for a scientific audience. The title and abstract are as follows:
我希望您能担任一名学术期刊编辑。我将为您提供我的手稿的标题和摘要。您需要为将手稿提交给《自然》杂志撰写一封格式正确的封面信。您应该声明该手稿尚未在任何其他期刊上考虑发表。简要介绍手稿的优点，并提供一���简短的总结，以向科学界突出研究结果的重要性。标题和摘要如下：[XXX]"""
        },
        "解释审稿人反馈": {
            "title": "解释审稿人反馈",
            "content": """这个指令可以帮你分析和解释审稿人对提交的研究论文的反馈，识别关键问题和建议。然后创建一个详细的回应计划，说明如何在修订稿中解决或反驳每个点。

Act as an academic research expert. Carefully analyze and interpret the [feedback] provided by the reviewer on the submitted research paper. Identify key concerns, constructive suggestions, and areas of improvement highlighted by the reviewer.
作为学术研究专家，分析审稿人的反馈并创建详细的回应计划。"""
        }
    }

def show_gpt_prompts():
    # 加载CSS样式
    load_css()
    
    # 获取提示词内容
    prompts_content = get_prompts_content()
    
    # 使用自定义样式的标题
    st.markdown('<h1 class="main-title">📚 学术论文写作 GPT 提示词</h1>', unsafe_allow_html=True)
    
    # 添加提醒信息
    st.info("⚠️ ps：GPT虽强但只是辅助，关键问题一定要自己斟酌之后再找其辅助")
    
    # 创建两列布局
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown('<h2 class="category-title">提示词分类</h2>', unsafe_allow_html=True)
        
        # 一、学术角色预设
        with st.expander("🎭 一、学术角色预设", expanded=True):
            st.info("""论文中无论是润色，语法检查还是降重，都要先进行角色预设...""")
            if st.button("👨‍🏫 1. 学术角色"):
                st.session_state.selected_prompt = prompts_content["学术角色"]
            if st.button("👨‍🔬 2. 论文评审专家"):
                st.session_state.selected_prompt = prompts_content["论文评审专家"]
        
        # 二、论文撰写指令
        with st.expander("✍️ 二、论文撰写指令"):
            prompts = ["写标题", "写英文标题", "写摘要", "写英文摘要", 
                      "缩写名称", "论文续写", "论文致谢", "论文大纲"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"📝 {i}. {prompt}", key=f"write_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
        
        # 三、学术润色指令
        with st.expander("🖌️ 三、学术润色指令"):
            prompts = ["英文润色1", "英文润色2", "中文润色", "SCI论文润色",
                      "期刊会议风格", "润色英文段落结构和句子逻辑", "直接润色段落", "多版本参考",
                      "错误纠正", "重新回答", "语法检查", "语法校正", 
                      "语法句法", "润色定位", "修改建议",
                      "修改意见", "封装基本事实/原理/背景", "逻辑论证辅助", "个性化润色"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"🖌️ {i}. {prompt}", key=f"polish_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
        
        # 四、中英翻译指令
        with st.expander("🌐 四、中英翻译指令"):
            prompts = ["论文翻译", "中译英1", "中译英2", "中译英3", "中英互译"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"🌐 {i}. {prompt}", key=f"translate_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
        
        # 五、论文查重降重指令
        with st.expander("🔍 五、论文查重降重指令"):
            prompts = ["内容降重", "改写降重", "同义词替换降重", "避免连续相同",
                      "缩写扩写降重", "关键词汇替换降重", "句式变换降重",
                      "逻辑重组", "综合改写", "概念解释降重"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"🔍 {i}. {prompt}", key=f"check_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
        
        # 六、参考文献指令
        with st.expander("📚 六、参考文献指令"):
            prompts = ["检查参考文献格式", "APA格式校正"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"📚 {i}. {prompt}", key=f"ref_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
        
        # 七、投稿审稿指令
        with st.expander("📝 七、投稿审稿指令"):
            prompts = ["撰写Cover letter", "解释审稿人反馈"]
            for i, prompt in enumerate(prompts, 1):
                if st.button(f"📝 {i}. {prompt}", key=f"submit_{i}"):
                    st.session_state.selected_prompt = prompts_content[prompt]
    
    with col2:
        st.markdown('<div class="prompt-detail">', unsafe_allow_html=True)
        if 'selected_prompt' in st.session_state:
            st.markdown(f"### 📋 {st.session_state.selected_prompt['title']}")
            prompt_content = st.text_area(
                "提示词内容",
                st.session_state.selected_prompt['content'],
                height=400
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📋 复制到剪贴板", use_container_width=True):
                    pyperclip.copy(prompt_content)
                    st.toast("✅ 已复制到剪贴板！")
            with col2:
                if st.button("💾 保存提示词", use_container_width=True):
                    save_prompt({
                        'title': st.session_state.selected_prompt['title'],
                        'content': prompt_content
                    })
                    st.toast("✅ 保存成功！")
        else:
            st.info("👈 请从左侧选择一个提示词")
        st.markdown('</div>', unsafe_allow_html=True)