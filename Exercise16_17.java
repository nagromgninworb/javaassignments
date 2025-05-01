import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.ScrollBar;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Exercise16_17 extends Application {
    private double red = 0, green = 0, blue = 0, opacity = 1;

    @Override
    public void start(Stage primaryStage) {
        Text text = new Text("JavaFX");
        text.setStyle("-fx-font-size: 40");

        ScrollBar sbRed = createScrollBar();
        ScrollBar sbGreen = createScrollBar();
        ScrollBar sbBlue = createScrollBar();
        ScrollBar sbOpacity = createScrollBar();
        sbOpacity.setValue(100);

        sbRed.valueProperty().addListener(e -> {
            red = sbRed.getValue() / 100.0;
            updateColor(text);
        });
        sbGreen.valueProperty().addListener(e -> {
            green = sbGreen.getValue() / 100.0;
            updateColor(text);
        });
        sbBlue.valueProperty().addListener(e -> {
            blue = sbBlue.getValue() / 100.0;
            updateColor(text);
        });
        sbOpacity.valueProperty().addListener(e -> {
            opacity = sbOpacity.getValue() / 100.0;
            updateColor(text);
        });

        VBox scrollBars = new VBox(10, sbRed, sbGreen, sbBlue, sbOpacity);
        BorderPane pane = new BorderPane();
        pane.setCenter(text);
        pane.setBottom(scrollBars);

        Scene scene = new Scene(pane, 400, 200);
        primaryStage.setTitle("Exercise16_17");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private ScrollBar createScrollBar() {
        ScrollBar sb = new ScrollBar();
        sb.setMin(0);
        sb.setMax(100);
        sb.setValue(0);
        sb.setPrefWidth(350);
        return sb;
    }

    private void updateColor(Text text) {
        text.setFill(new Color(red, green, blue, opacity));
    }

    public static void main(String[] args) {
        launch(args);
    }
}
