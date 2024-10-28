import torch
import torch.nn as nn

input_dim = 28*28
output_dim = 10
hidden_dim = 20

class ClimateControlModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(ClimateControlModel, self).__init__()
        # Linear function
        self.fc1 = nn.Linear(input_dim, hidden_dim) 

        # Non-linearity
        self.sigmoid = nn.Sigmoid()

        # Linear function (readout)
        self.fc2 = nn.Linear(hidden_dim, output_dim)  
        criterion = nn.CrossEntropyLoss()

    def forward(self, x):
        # Linear function  # LINEAR
        out = self.fc1(x)

        # Non-linearity  # NON-LINEAR
        out = self.sigmoid(out)

        # Linear function (readout)  # LINEAR
        out = self.fc2(out)
        return out
    

def train():
    model = ClimateControlModel(input_dim, output_dim)
    iter = 0

    num_epochs = 20

    learning_rate = 0.1

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    batch_size = 100
    n_iters = 3000

    train_dataset = []
    batch_size = 1
    test_dataset = []
    num_epochs = n_iters / (len(train_dataset) / batch_size)
    num_epochs = int(num_epochs)

    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                            batch_size=batch_size, 
                                            shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                                            batch_size=batch_size, 
                                            shuffle=False)

    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            # Load images with gradient accumulation capabilities
            images = images.view(-1, 28*28).requires_grad_()

            # Clear gradients w.r.t. parameters
            optimizer.zero_grad()

            # Forward pass to get output/logits
            outputs = model(images)

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
                for images, labels in test_loader:
                    # Load images with gradient accumulation capabilities
                    images = images.view(-1, 28*28).requires_grad_()

                    # Forward pass only to get logits/output
                    outputs = model(images)

                    # Get predictions from the maximum value
                    _, predicted = torch.max(outputs.data, 1)

                    # Total number of labels
                    total += labels.size(0)

                    # Total correct predictions
                    correct += (predicted == labels).sum()

                accuracy = 100 * correct / total

                # Print Loss
                print('Iteration: {}. Loss: {}. Accuracy: {}'.format(iter, loss.item(), accuracy))

def finished_model():
    model = ClimateControlModel(input_dim, output_dim)
    return model

def inputs_to_vector(inputs):
    return torch.tensor(inputs)