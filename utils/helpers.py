import json
import os

# 确保数据目录存在
def ensure_data_dir():
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir

def save_prompt(prompt):
    """保存提示词到文件"""
    data_dir = ensure_data_dir()
    prompts_file = os.path.join(data_dir, 'prompts.json')
    prompts = load_prompts()
    prompts.append(prompt)
    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

def load_prompts():
    """加载提示词列表"""
    data_dir = ensure_data_dir()
    prompts_file = os.path.join(data_dir, 'prompts.json')
    if not os.path.exists(prompts_file):
        return []
    with open(prompts_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_chat_history(chat):
    """保存聊天历史"""
    data_dir = ensure_data_dir()
    history_file = os.path.join(data_dir, 'chat_history.json')
    history = load_chat_history()
    history.append(chat)
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_chat_history():
    """加载聊天历史"""
    data_dir = ensure_data_dir()
    history_file = os.path.join(data_dir, 'chat_history.json')
    if not os.path.exists(history_file):
        return []
    with open(history_file, 'r', encoding='utf-8') as f:
        return json.load(f) 