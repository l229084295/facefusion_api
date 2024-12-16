import sys
import subprocess

def swap_face(source_image, target_image, output_image) -> None:
	commands = [sys.executable, 'facefusion.py', 'headless-run',
			 '--processors', 'face_swapper', 'face_enhancer',
			 '--execution-providers', 'cuda', # 'cpu', 'tensorrt',
			 '-s', 'images/' + source_image, '-t', 'images/' + target_image,
			 '-o', 'images/' + output_image]
	# print(commands)

	run = subprocess.run(commands, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	print("STDOUT:", run.stdout.decode())
	# print("STDERR:", run.stderr.decode())

	assert run.returncode == 0
	assert 'image succeed' in run.stdout.decode()

if __name__ == '__main__':
	swap_face("1.jpg",
			   "2.jpg",
			  "3.jpg")
