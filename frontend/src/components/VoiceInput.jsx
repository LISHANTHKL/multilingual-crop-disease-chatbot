import SpeechRecognition, {
  useSpeechRecognition
} from "react-speech-recognition";

export default function VoiceInput({
  onText
}) {

  const {
    transcript,
    resetTranscript
  } = useSpeechRecognition();

  const startListening = () => {

    resetTranscript();

    SpeechRecognition.startListening({
      continuous: false
    });
  };

  const stopListening = () => {

    SpeechRecognition.stopListening();

    onText(transcript);
  };

  return (
    <div>

      <button
        className="btn btn-success"
        onClick={startListening}
      >
        🎤 Start
      </button>

      <button
        className="btn btn-danger ms-2"
        onClick={stopListening}
      >
        Stop
      </button>

    </div>
  );
}