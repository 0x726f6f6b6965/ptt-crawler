from ptt_crawler import get_context
import argparse, json

def parse_args():
    parser = argparse.ArgumentParser(description="PTT Content Crawler Tool")
    parser.add_argument("-u", "--url", type=str, default="", help="the PTT content URL")
    parser.add_argument("--headers" , type=dict, default="", help="the request headers")
    parser.add_argument("-o", "--output" , type=str, default="", help="the output path")
    parser.add_argument("-p", "--print", action='store_true', help="Print the result")
    return parser.parse_args()

def main():
    arguments = parse_args()
    if arguments.url == '':
        print("Please enter the PTT URL")
        return
    resp = get_context(arguments.url, arguments.headers)
    if arguments.print:
        print(json.dumps(resp, ensure_ascii=False).encode('utf8').decode())
    if arguments.output != '':
        path = arguments.output 
        with open(path, 'w', encoding='utf8') as f:
            json.dump(resp, f, ensure_ascii=False)
        

if __name__ == '__main__':
    main()