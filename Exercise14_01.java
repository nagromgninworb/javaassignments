import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Exercise14_01 extends Application {
    @Override
    public void start(Stage primaryStage) {
        GridPane pane = new GridPane();

        String[] flags = {
            "https://liveexample.pearsoncmg.com/book/image/flag1.gif",
            "https://liveexample.pearsoncmg.com/book/image/flag2.gif",
            "https://liveexample.pearsoncmg.com/book/image/flag6.gif",
            "https://liveexample.pearsoncmg.com/book/image/flag7.gif"
        };

        for (int i = 0; i < flags.length; i++) {
            Image image = new Image(flags[i]);
            ImageView imageView = new ImageView(image);
            imageView.setFitWidth(150);
            imageView.setFitHeight(100);
            pane.add(imageView, i % 2, i / 2);
        }

        Scene scene = new Scene(pane);
        primaryStage.setTitle("Exercise14_01");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
