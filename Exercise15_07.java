import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class Exercise15_07 extends Application {
    @Override
    public void start(Stage primaryStage) {
        Circle circle = new Circle(150, 150, 75);
        circle.setFill(Color.WHITE);
        circle.setStroke(Color.BLACK);

        circle.setOnMousePressed((MouseEvent e) -> {
            circle.setFill(Color.BLACK);
        });

        circle.setOnMouseReleased((MouseEvent e) -> {
            circle.setFill(Color.WHITE);
        });

        Pane pane = new Pane(circle);
        Scene scene = new Scene(pane, 300, 300);
        primaryStage.setTitle("Exercise15_07");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
