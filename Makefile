
dev:
	docker run --rm -v .:/root/ -p 51111:51111 annatarhe/face_recognition:v1.2.3 python /root/main.py

.PHONY: pb
pb:
	python -m grpc_tools.protoc -I./protos --python_out=./pb --grpc_python_out=./pb ./protos/face.proto