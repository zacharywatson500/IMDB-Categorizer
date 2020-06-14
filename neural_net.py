import torch 
from torch import autograd, nn 
import torch.nn.functional as F

batch_size = 5 
input_size = 3
hidden_size = 4 
num_classes = 2 


input = torch.rand(batch_size,input_size)
print("input: ",input)

class N_Net(nn.Module):
	def __init__(self,input_size, hidden_size, num_classes): #create hidden layers
		super().__init__()
		self.h1 = nn.Linear(input_size, hidden_size) 
		print("h1: ",self.h1)
		self.h2 = nn.Linear(hidden_size, num_classes) 
		print("h2: ",self.h1)

	def forward(self, x): 
		x = self.h1(x)
		x = F.tanh(x)
		x = self.h2(x)
		return x 

model = N_Net(input_size=input_size, hidden_size=hidden_size,num_classes=num_classes)
out = N_Net(input_size, hidden_size, num_classes)
print('Out: ',out)