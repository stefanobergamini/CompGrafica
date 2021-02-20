install: 
	pip install PyQt5 && pip install pyclean && pip install numpy && make run

run:
	pyclean -v . && python ./main.py