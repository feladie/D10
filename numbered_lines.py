#!/usr/bin/env python3
def numbered_lines():
	result = open('numbered_lines.txt', 'w')
	count = 1
	with open('small.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			if len(line) > 1:
				line = line.strip()
				result.write(str(count) + ' ' + line + '\n')
				count += 1
	result.close()


def main():
    numbered_lines()

if __name__ == "__main__":
    main()
