import js2py

js = '''var shortestPath = function(start, end) {
            var queue = [start];
            var visited = {};
            var path = {};
            var current;
            while (queue.length > 0) {
                current = queue.shift();
                if (current === end) {
                break;
                }
                visited[current] = true;
                for (var i = 0; i < current.neighbors.length; i++) {
                if (!visited[current.neighbors[i]]) {
                    queue.push(current.neighbors[i]);
                    path[current.neighbors[i]] = current;
                }
                }
            }
            var result = [];
            while (current !== start) {
                result.push(current);
                current = path[current];
            }
            result.push(start);
            return result.reverse();
        };'''
        
result = js2py.eval_js(js)
print(result)
