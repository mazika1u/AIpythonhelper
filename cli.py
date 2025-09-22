import argparse
from ai_helper.generator import generate_code
from ai_helper.optimizer import improve_code
from ai_helper.executor import run_code

parser = argparse.ArgumentParser()
parser.add_argument("--generate", type=str, help="生成するコードの説明")
parser.add_argument("--improve", type=str, help="改善したい既存コード")
parser.add_argument("--run", type=str, help="実行したいコード")
args = parser.parse_args()

if args.generate:
    print(generate_code(args.generate))
elif args.improve:
    print(improve_code(args.improve))
elif args.run:
    print(run_code(args.run))
