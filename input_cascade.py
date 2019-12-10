def input_cascade(input_shape1,input_shape2):
  
  X1_input = Input(input_shape1)
  # 1st two-path of cascade
  X1 = two_path(X1_input)
  X1 = Conv2D(5,(21,21),strides=(1,1),padding='valid',activation='relu', kernel_regularizer=regularizers.l2(0.01),
               activity_regularizer=regularizers.l1(0.01))(X1)
  X1 = BatchNormalization()(X1)
  
  X2_input = Input(input_shape2)
  # Concatenating the output of 1st to input of 2nd
  X2_input1 = Concatenate()([X1,X2_input])
  X2 = two_path(X2_input1)
  
  # Fully convolutional softmax classification including L1/L2 regularization
  X2 = Conv2D(5,(21,21),strides=(1,1),padding='valid',  kernel_regularizer=regularizers.l2(0.01),
               activity_regularizer=regularizers.l1(0.01))(X2)
  X2 = BatchNormalization()(X2)
  #X2 = Flatten()(X2)
  X2 = Activation('softmax')(X2)
  
  model = Model(inputs=[X1_input,X2_input],outputs=X2)
  return model