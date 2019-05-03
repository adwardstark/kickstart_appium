### Testing apps using appium

This project contains examples for testing Android, iOS applications using the appium testing framework.

#### Pre-requisites

To run these samples you need to install the core components like Android SDK, Xcode( for iOS ) on your machine along with the following tools:

- Appium
  ```bash
  npm install -g appium
  ```
- Python
  ```bash
  brew install python
  ```
- Appium Python Client
  ```bash
  pip install Appium-Python-Client
  ```
- PyTest
  ```bash
  pip install -U pytest
  ```
- Carthage ( for iOS )
  ```bash
  brew install carthage
  ```

#### Building iOS Project

To prepare the app for testing, build it with a specific SDK using `XcodeBuild`. Assuming you’ve changed to your Xcode project folder, type the following command to create the build:
```bash
xcodebuild -sdk iphonesimulator12.2
```
This will compile the project and create the build under the build folder. You can find a `build/Release-iphonesimulator` directory that contains the `.app` package that you’ll need to communicate with the Appium server.

#### Building Android Project

To prepare the app for testing, build it using gradlew. Assuming you’ve changed to your android project folder, type the following command to create the build:
```bash
./gradlew assemble
```
This will compile the project and create the build under the `build/outputs/apk` folder. You can find the `.apk` package that you’ll need to communicate with the Appium server.

#### Running Tests

Now is the moment to run the tests but you need to start `appium` server first. In Terminal, execute the command below:
```bash
appium
```

To execute the following tests ( Android/iOS ) switch to the `/Tests` directory of the project and type the following command to execute the tests:

- iOS
  ```bash
  pytest test_ios.py
  ```
- Android

  Make sure to set `ANDROID_HOME` environment variable pointing to the `Android SDK` and then start the emulator which you've specified in the `test_android.py` file before executing the command below.
  ```bash
  pytest test_android.py
  ```

You should see a message specifying the time taken to execute the test and how many of the test cases passed/failed.

#### Voila!

You deserve a pat on your back for following through this lengthy process to get your appium tests running!