import TextAnalyzer from "./pages/TextAnalyzer";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center p-6">
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-lg p-8 space-y-5">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-slate-800">
            HateShield AI
          </h1>
          <p className="text-slate-500 text-sm mt-1">
            Multilingual Hate Speech Detection
          </p>
        </div>
        <TextAnalyzer />
      </div>
    </div>
  );
}
