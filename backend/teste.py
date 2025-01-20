import torch
import whisper

model = whisper.load_model("base")
print("Modelo de IA carregado com sucesso!")

print(torch.version)