// src/pages/TextAnalyzer.jsx
import { useState } from "react";
import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export default function TextAnalyzer() {
  const [text, setText] = useState("");
  const [language, setLanguage] = useState("auto");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    setError("");
    setResult(null);

    if (!text.trim()) {
      setError("Please enter some text");
      return;
    }

    try {
      setLoading(true);
      const res = await axios.post(`${API_BASE}/analyze`, {
        text,
        language,
      });
      setResult(res.data.result);
    } catch {
      setError("Backend connection failed.");
    } finally {
      setLoading(false);
    }
  };

  const severityColor = (val) => {
    if (val >= 0.75) return "bg-red-500";
    if (val >= 0.45) return "bg-orange-400";
    return "bg-emerald-500";
  };

  return (
    <div className="space-y-6">

      {/* TEXT INPUT */}
      <textarea
        className="w-full h-36 border border-slate-300 rounded-xl p-4 text-sm resize-none outline-none focus:ring-2 focus:ring-slate-500"
        placeholder="Paste or type any text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      {/* CONTROLS ROW */}
      <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">

        <div className="w-full sm:w-48">
          <label className="block text-sm text-slate-500 mb-1">
            Language
          </label>
          <select
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="auto">Auto detect</option>
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="gu">Gujarati</option>
          </select>
        </div>

        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="w-full sm:w-auto bg-slate-900 hover:bg-slate-700 text-white px-6 py-3 rounded-xl transition disabled:bg-slate-400"
        >
          {loading ? "Analyzing…" : "Analyze"}
        </button>

      </div>

      {/* ERROR */}
      {error && (
        <div className="p-3 bg-red-100 text-red-600 rounded-lg text-sm">
          {error}
        </div>
      )}

      {/* RESULT */}
      {result && (

        <div className="border border-slate-200 rounded-xl p-5 space-y-3 bg-slate-50">

          <div className="flex justify-between items-center">
            <p className="font-semibold">
              Prediction:
              {result.is_hate ? (
                <span className="text-red-600 ml-2">Hate Speech</span>
              ) : (
                <span className="text-green-600 ml-2">Not Hate</span>
              )}
            </p>

            <p className="text-sm">
              Confidence:
              <span className="font-bold ml-1">
                {Math.round(result.confidence * 100)}%
              </span>
            </p>
          </div>

          <p>
            Category:{" "}
            <span className="font-medium text-slate-700">
              {result.category}
            </span>
          </p>

          {/* SEVERITY BAR */}
          <div>
            <p className="text-sm mb-1">
              Severity: {Math.round(result.severity * 100)}%
            </p>
            <div className="h-3 w-full bg-slate-200 rounded-full">
              <div
                className={`h-full ${severityColor(result.severity)} rounded-full`}
                style={{ width: `${result.severity * 100}%` }}
              />
            </div>
          </div>

          <p>
            Language detected:{" "}
            <span className="font-medium text-slate-700">
              {result.language}
            </span>
          </p>

          <p className="text-slate-600 text-sm">
            {result.explanation}
          </p>

        </div>
      )}

    </div>
  );
}
