from keras.layers import Input, Dense, Reshape, Flatten
from keras.layers import BatchNormalization
from keras.layers import LeakyReLU
from keras.models import Sequential, Model
import numpy as np
from keras.optimizers.legacy import Adam


LATENT_DIM = 100
DATA_SHAPE = (480, 128)
OPTIMIZER = Adam(0.0002, 0.5)


def build_generator():

    model = Sequential()

    model.add(Dense(256, input_dim=LATENT_DIM))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(1024))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(np.prod(DATA_SHAPE), activation='sigmoid'))
    model.add(Reshape(DATA_SHAPE))

    model.summary()

    noise = Input(shape=(LATENT_DIM,))
    img = model(noise)

    return Model(noise, img)
    

def build_discriminator():

    model = Sequential()

    model.add(Flatten(input_shape=DATA_SHAPE))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(256))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.summary()

    img = Input(shape=DATA_SHAPE)
    validity = model(img)

    return Model(img, validity)


def create_model():

    # Create the discriminator
    discriminator = build_discriminator()
    discriminator.compile(loss='binary_crossentropy',
        optimizer=OPTIMIZER,
        metrics=['accuracy'])
    
    # Create the generator
    generator = build_generator()

    # The generator takes noise as input and generates imgs
    z = Input(shape=(LATENT_DIM,))
    img = generator(z)

    # For the combined model we will only train the generator
    discriminator.trainable = False
    # The discriminator takes generated images as input and determines validity
    validity = discriminator(img)
    
    combined = Model(z, validity)
    # The combined model  (stacked generator and discriminator)
    # Trains the generator to fool the discriminator
    combined.compile(loss='binary_crossentropy', optimizer=OPTIMIZER)
    
    return discriminator, generator, combined
    


class GAN():
    def __init__(self, Train:bool=True) -> None:
        self.discriminator, self.generator, self.combined  = create_model()
        if not Train:
            self.generator.load_weights("save/generator_weights.h5")
            self.discriminator.load_weights("save/discriminator_weights.h5")
            self.combined.load_weights("save/combined_weights.h5")

    def train(self, epochs:int, X_train:list, batch_size:int=128, sample_interval:int=50):
        # Adversarial ground truths
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        for epoch in range(epochs):

            # Select a random batch of images
            idx = np.random.randint(0, X_train.shape[0], batch_size)
            imgs = X_train[idx]

            # Generate a batch of new images
            noise = np.random.normal(0, 1, (batch_size, LATENT_DIM))
            gen_imgs = self.generator.predict(noise)

            # Train the discriminator
            d_loss_real = self.discriminator.train_on_batch(imgs, valid) # Learn to recognize real images
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake) # Learn to recognize fake images
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake) # Average the two losses

            noise = np.random.normal(0, 1, (batch_size, LATENT_DIM))

            # Train the generator (to have the discriminator label samples as valid)
            g_loss = self.combined.train_on_batch(noise, valid)

            # Plot the progress
            print ("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss))

            # If at save interval => save generated image samples
            if epoch % sample_interval == 0:
                # sample_images(epoch, self.generator)
                pass
        
    def predict(self) -> np.ndarray:
        noise = np.random.normal(0, 1, (1, LATENT_DIM))
        return self.generator.predict(noise)

