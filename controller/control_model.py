import torch
import torch.nn as nn
from data import load_data

input_dim = 13
output_dim = 3
hidden_dim = 20

class ClimateControlModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(ClimateControlModel, self).__init__()
        # Linear function
        self.fc1 = nn.Linear(input_dim, hidden_dim) 
        fchalf_dim = 30
        self.fc1half = nn.Linear(hidden_dim, fchalf_dim) 

        # Non-linearity
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()

        # Linear function (readout)
        self.fc2 = nn.Linear(fchalf_dim, output_dim)  

    def forward(self, x):
        # Linear function  # LINEAR
        x = self.relu(self.fc1(x))
        x = self.fc1half(x)

        # Non-linearity  # NON-LINEAR
        x = self.relu(x)

        # Linear function (readout)  # LINEAR
        out = self.fc2(x)
        out = self.sigmoid(out)
        return out
    
    def load(self, name='models/brain'):
        self.load_state_dict(torch.load(name))
        print('Loaded model from {}!'.format(name))

    def save(self, name='models/brain'):
        torch.save(self.state_dict(), name)
        print('Saved model to {}!'.format(name))
    


def train(model):
    iter = 0

    learning_rate = 0.1

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    n_iters = 4500

    criterion = nn.BCELoss()

    train_dataset = load_data()
    batch_size = 20
    test_dataset = train_dataset
    num_epochs = n_iters / (len(train_dataset) / batch_size)
    num_epochs = int(num_epochs)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                            batch_size=batch_size, 
                                            shuffle=True)

    # test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
    #                                         batch_size=batch_size, 
    #                                         shuffle=False)

    for epoch in range(num_epochs):
        for i, (vec, labels) in enumerate(train_dataset):
            # vec, labels = data
            vec = torch.as_tensor(vec)
            labels = torch.as_tensor(labels)

            # Clear gradients w.r.t. parameters
            optimizer.zero_grad()

            # Forward pass to get output/logits
            outputs = model(vec)

            # Calculate Loss: softmax --> cross entropy loss
            loss = criterion(outputs, labels)

            # Getting gradients w.r.t. parameters
            loss.backward()

            # Updating parameters
            optimizer.step()

            iter += 1

            if iter % 500 == 0:
                # Calculate Accuracy         
                correct = 0
                total = 0
                # Iterate through test dataset
                for vec2, labels2 in train_dataset:
                    vec2 = torch.as_tensor(vec2)

                    # Forward pass only to get logits/output
                    outputs = model(vec2)

                    # Get predictions from the maximum value
                    total += 1
                    ac_on = 0
                    heat_on = 0
                    if outputs[1] > 0.5:
                        ac_on = 1
                    if outputs[2] > 0.5:
                        heat_on = 1

                    if labels2[1] == ac_on and labels2[2] == heat_on:
                        correct += 1

                accuracy = 100 * correct / total

                # Print Loss
                print('Iteration: {}. Loss: {}. Accuracy: {}'.format(iter, loss.item(), accuracy))

    # Final test
    correct = 0
    total = 0
    for vec2, labels2 in train_dataset:
        vec2 = torch.as_tensor(vec2)

        # Forward pass only to get logits/output
        outputs = model(vec2)

        # Get predictions from the maximum value
        total += 1
        ac_on = 0
        heat_on = 0
        if outputs[1] > 0.5:
            ac_on = 1
        if outputs[2] > 0.5:
            heat_on = 1

        if labels2[1] == ac_on and labels2[2] == heat_on:
            # print(labels2, ac_on, heat_on, outputs)
            correct += 1

    accuracy = 100 * correct / total

    # Print Loss
    print('Iteration: {}. Loss: {}. Accuracy: {}'.format(iter, loss.item(), accuracy))
    model.save()

def finished_model():
    model = ClimateControlModel(input_dim, output_dim)
    model.load()
    return model

def inputs_to_vector(inputs):
    return torch.tensor(inputs)

if __name__ == "__main__":
    model = ClimateControlModel(input_dim, output_dim)
    train(model)