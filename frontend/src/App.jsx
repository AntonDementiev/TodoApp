import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [todos, setTodos] = useState([]);
  const [newHeader, setNewHeader] = useState("");
  const [newBody, setNewBody] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/todo/list");
      setTodos(response.data);
    } catch (error) {
      setError("");
    } finally {
      setLoading(false);
    }
  };

  const addTodo = async () => {
    if (!newHeader.trim() || !newBody.trim()) return;  // Проверка на пустые поля
    try {
      const response = await axios.post("http://localhost:8000/todo/create", {
        header: newHeader,
        body: newBody,
      });
      setTodos([...todos, response.data]);
      setNewHeader("");  // Очистка поля заголовка
      setNewBody("");  // Очистка поля описания
    } catch (error) {
      setError("Что-то пошло не так");
    }
  };

  const deleteTodo = async (todoId) => {
    try {
      await axios.delete(`http://localhost:8000/todo/delete/${todoId}`);
      setTodos(todos.filter((todo) => todo.todo_id !== todoId));
    } catch (error) {
      setError("Что-то пошло не так");
    }
  };

  return (
    <div className="app">
      <h2>Мои задачи</h2>
      <div className="todo-input">
        <input
          type="text"
          value={newHeader}
          onChange={(e) => setNewHeader(e.target.value)}
          placeholder="Заголовок"
        />
        <textarea
          value={newBody}
          onChange={(e) => setNewBody(e.target.value)}
          placeholder="Описание задачи"
        />
        <button onClick={addTodo}>Добавить</button>
      </div>
      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <ul className="todo-list">
          {todos.map((todo) => (
            <li key={todo.todo_id} className="todo-item">
              <div className="todo-header">{todo.header}</div> {/* Заголовок задачи */}
              <div className="todo-body">{todo.body}</div> {/* Описание задачи */}
              <button onClick={() => deleteTodo(todo.todo_id)}>Удалить</button>
            </li>
          ))}
        </ul>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;
