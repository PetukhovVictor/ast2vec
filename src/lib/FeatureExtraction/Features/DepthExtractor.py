import numpy


class DepthExtractor:
    metrics = {
        'mean': numpy.mean,
        'min': numpy.min,
        'max': numpy.max
    }

    def __init__(self, metric):
        self.metric = metric

    def dfs(self, nodes, depths, path_number):
        if len(depths) <= path_number:
            depths.append(1)
        else:
            depths[path_number] += 1
        for node in nodes:
            if 'children' in node:
                depths = self.dfs(node['children'], depths, path_number)
            path_number += 1

        return depths

    def extract(self, ast):
        depths = self.dfs(ast, [], 0)

        return self.metrics[self.metric](depths)
