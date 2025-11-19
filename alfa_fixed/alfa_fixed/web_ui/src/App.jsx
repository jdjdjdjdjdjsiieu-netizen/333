import React, { useEffect, useState } from 'react'

export default function App() {
  const [config, setConfig] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/config/')
      .then((r) => r.json())
      .then((data) => setConfig(data))
      .catch(() => setConfig(null))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div style={{ fontFamily: 'Arial, Helvetica, sans-serif', padding: 40 }}>
      <h1>Alfa — Setup UI</h1>
      <p>
        Небольшой быстрый интерфейс для просмотра текущих настроек окружения.
      </p>
      {loading ? (
        <p>Загрузка...</p>
      ) : config ? (
        <div>
          <h3>Текущая конфигурация (маскированная):</h3>
          <pre>{JSON.stringify(config, null, 2)}</pre>
        </div>
      ) : (
        <p>Не удалось загрузить config.</p>
      )}
    </div>
  )
}
