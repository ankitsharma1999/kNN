class kNN:
	
	def __init__(self, x_train, y_train, k=5):
		self.k = k
		self.x_train = x_train
		self.y_train = y_train
	
	def predict(self, x_test):
		
		dist = self.distance(self.x_train, x_test)
		labels = self.y_train
		
		dist, labels = zip(*sorted(zip(dist, labels)))
		top_k_entries = labels[0:self.k]
		classes = self.unique(top_k_entries)
		
		pred = max(set(classes), key=classes.count)
		return pred
	
	def distance(self, x_train, x_test):
		
		dist = []
		x = x_test[0]
		y = x_test[1]
		for j in range(len(x_train)):
			d = (((x_train[j][0] - x) ** 2) + ((x_train[j][1] - y) ** 2))**0.5
			dist.append(d)
		
		return dist
	
	def unique(self, list1):
		
		unique_list = []
		
		for x in list1:
			if x not in unique_list:
				unique_list.append(x)
		
		return unique_list
