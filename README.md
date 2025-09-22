# AIpythonhelper

Python用のAIコード補助ツールです。
このツールを使うと、簡単にPythonコードを生成・改善・実行できます。
CLIからもPythonscriptからも操作可能です。

---

## 目次

1. [概要](#概要)
2. [インストール方法](#インストール方法)
3. [初期設定](#初期設定)
4. [使用方法](#使用方法)

   * [Pythonから使用](#pythonから使用)
   * [CLIから使用](#cliから使用)
5. [設定・変更が必要な箇所](#設定変更が必要な箇所)
6. [実用的な使い方の例](#実用的な使い方の例)
7. [注意事項](#注意事項)
8. [拡張アイデア](#拡張アイデア)
9. [FAQ](#faq)
10. [ライセンス](#ライセンス)

---

## 概要

`AIpythonhelper` は Pythonの学習や開発をサポートするAIツールです。
OpenAI APIを利用して以下のことが可能です：

* プロンプトからPythonコードを自動生成
* 既存コードの改善・最適化
* Pythonコードの安全な実行
* CLI・Pythonscriptからの操作

> **対象ユーザー**: Python学習者、開発者、コード補助をAIで自動化したい方

---

## インストール方法

1. リポジトリをクローンします:

```bash
git clone https://github.com/<ユーザ名>/AIpythonhelper.git
cd AIpythonhelper
```

2. 必要なライブラリをインストールします:

```bash
pip install -r requirements.txt
```

> Python 3.10以上を推奨

---

## 初期設定

1. **OpenAI APIkeyの取得**

   * [OpenAI公式サイト](https://platform.openai.com/account/api-keys)でAPIkeyを発行
   * セキュリティ上、**環境変数**で設定することを推奨:

```bash
export OPENAI_API_KEY="あなたのAPIkey"
```

2. `ai_helper/generator.py` を編集して直接APIkeyを指定することも可能:

```python
client = OpenAI(api_key="YOUR_API_KEY")  # ←ここを自分のkeyに変更
```

3. **タイムアウト設定**

   * `executor.py` の `timeout=5` は短時間実行用
   * 長いコードの場合は適宜変更してください

4. **モデルの変更**

   * デフォルトは `"gpt-5-mini"`
   * より精度を上げたい場合は `"gpt-5"` や `"gpt-4o"` に変更可能

---

## 使用方法

### Pythonから使用

#### コード生成

```python
from ai_helper.generator import generate_code

prompt = "PythonでFizzBuzz関数を書いて"
code = generate_code(prompt)
print(code)
```

#### コード改善

```python
from ai_helper.optimizer import improve_code

existing_code = """
def f(x):
    for i in range(x):
        print(i)
"""
improved = improve_code(existing_code, prompt="可読性と効率を向上させてください")
print(improved)
```

#### コード実行

```python
from ai_helper.executor import run_code

code = "print('Hello World')"
result = run_code(code)
print(result)
```

---

### CLIから使用

```bash
# コード生成
python cli.py --generate "Pythonで二分探索関数を書いて"

# コード改善
python cli.py --improve "既存コードを改善して"

# コード実行
python cli.py --run "print('Hello CLI')"
```

> CLIはPythonscriptに依存せず、簡単に生成→改善→実行まで可能

---

## 設定・変更が必要な箇所

1. **APIkey**

   * `ai_helper/generator.py` に直接書くか、環境変数で設定
2. **モデル**

   * `generate_code()` 内の `model` を変更可能
3. **タイムアウト**

   * `executor.py` の `timeout` パラメータを変更
4. **CLI拡張**

   * 好きなプロンプトやオプションを追加可能
5. **コードキャッシュ・スニペット管理**

   * `ai_helper/utils.py` を利用してよく使うコードを保存可能

---

## 実用的な使い方の例

1. **関数テンプレートの自動生成**

```bash
python cli.py --generate "Pythonでファイル操作の関数を書いて"
```

2. **既存コードの効率化**

```bash
python cli.py --improve "長いforループのコードを改善"
```

3. **簡単な学習環境**

* Python学習者が思いついた処理をCLIで生成し、実行結果を即確認可能

---

## 注意事項

* 自動生成コードは必ず確認して使用してください
* APIkeyは公開しないこと
* 大量リクエストはAPI制限に注意
* 実行コードの安全性は保証されません（sandboxでの実行推奨）
* Python 3.10以上推奨

---

## 拡張アイデア

* GUI化（Tkinter / PySimpleGUI）
* 複数言語対応（JavaScript, HTMLなど）
* localsnippetの保存・検索機能
* CLIのプロンプト履歴管理
* GitHub Gist連携でコードを直接保存

---

## FAQ

**Q1: APIkeyを複数人で共有できますか？**
A1: 共有は推奨されません。各自のAPIkeyを使うこと。

**Q2: 実行結果が出ない場合は？**
A2: タイムアウトや環境変数設定を確認してください。

**Q3: 生成コードがエラーになる場合は？**
A3: プロンプトを具体的に書き、必要に応じて改善をCLIで実行してください。

---
