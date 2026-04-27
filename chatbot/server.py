from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from main_server import Natural_Language_Processing


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path.endswith('.css'):
            self._set_response(200, 'text/css')
            with open(self.path[1:], 'rb') as css_file:
                self.wfile.write(css_file.read())
            return
        elif self.path.endswith('.png'):  # Handle .png image requests
            self._set_response(200, 'image/png')
            with open(self.path[1:], 'rb') as image_file:
                self.wfile.write(image_file.read())
            return
        try:
            file_to_open = open(self.path[1:], 'r', encoding='utf-8').read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self._set_response()
        self.wfile.write(file_to_open.encode('utf-8'))

    def do_POST(self):
        # 尝试从POST请求中获取数据长度
        print(self.headers['Content-Length'])
        content_length = int(self.headers['Content-Length'])
        print(content_length)
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        print(post_data)
        print(data)
        try:
            # 从JSON数据中提取所需的信息
            query = data['query']
            # 调用main_server函数中的
            answer = Natural_Language_Processing(query)
            print(answer)
            response = {'answer': answer}
            self._set_response(200, 'application/json')
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except:
            self._set_response(400, 'application/json')
            self.wfile.write(json.dumps({'error': 'Invalid input'}).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='0.0.0.0', port=8000):
    # 使用'0.0.0.0'作为host可以让服务器监听所有可用的网络接口
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on {host}:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down.")
        httpd.server_close()


if __name__ == '__main__':
    run()
