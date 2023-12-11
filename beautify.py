import sys

def beautify(filename):
    
    with open(filename, 'r') as f:
        lines = f.readlines()

        cols = 0
        start = end = -1
        tables = []

        # Find which lines contain tables
        for i, line in enumerate(lines):
            n = line.count('|')
            if n != 0 and cols == 0:
                cols = n - 1
                start = i

            elif n != 0 and cols == n - 1:
                end = i

            elif n == 0 and start != -1 and end != -1:
                tables.append((start, end, cols))
                cols = 0
                start = end = -1

        # Beautify table
        new_lines = lines
        for table in tables:
            start, end, cols = table

            # Find max space used per column
            max_space = {col: 0 for col in range(cols)}
            for line in lines[start:end+1]:
                content = line.split('|')[1:-1]
                for col in range(cols):
                    max_space[col] = max(max_space[col], len(content[col]))

            # Pad with white spaces
            for i in range(start, end+1):
                content = new_lines[i].split('|')
                for col, max_len in max_space.items():
                    if i == start + 1:
                        content[col + 1] = content[col + 1][:-1] + '-'*(max_len - len(content[col + 1])) + ' '
                    else:
                        content[col + 1] = content[col + 1] + ' '*(max_len - len(content[col + 1]))
                new_lines[i] = '|'.join(content)

    with open(filename, 'w') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    filename = sys.argv[1]
    beautify(filename)
    