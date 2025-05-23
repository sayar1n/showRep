"use client";

import Link from "next/link";
import styles from "./page.module.scss";
import axios from "axios";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function SignUp() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const api = axios.create({
    baseURL: "http://localhost:8061",
    withCredentials: true,
    headers: {
      "Content-Type": "application/json",
    },
  });
  // Функция для обработки регистрации
  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await api.post("/auth/register", {
        username,
        email,
        password,
      });

      if (response.status === 200) {
        router.push("/auth/signIn");
      }
    } catch (error: any) {
      // Обработка ошибок API
      if (error.response && error.response.data && error.response.data.detail) {
        const detail = error.response.data.detail;
        if (Array.isArray(detail)) {
          const errorMessages = detail.map((err: any) => err.msg).join(", ");
          setError(errorMessages);
        } else {
          setError(detail);
        }
      } else {
        setError("Ошибка регистрации.");
      }
      console.error("Ошибка:", error);
    }
  };

  return (
    <div className={styles.signInBlock}>
      <div className={styles.formSection}>
        {/* Блок загаловка регистрации */}
        <div className={styles.titleBlock}>
          <div className={styles.logo}>Articly</div>
          <span>Зарегистрируйтесь,<br />чтобы начать пользоваться приложением</span>
        </div>

        {/* Основная форма регистрации */}
        <form onSubmit={handleRegister}>
          <div className={styles.inputField}>
            {/* Поле ввода nickname */}
            <div className={styles.inputNickname}>
              <label className={styles.label}>Никнейм:</label>
              <input
                type="text"
                className={styles.nicknameInputBox}
                placeholder="Ваш никнейм"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            {/* Поле ввода email */}
            <div className={styles.inputEmail}>
              <label className={styles.label}>Почта:</label>
              <input
                type="email"
                className={styles.emailInputBox}
                placeholder="email@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            {/* Поле ввода пароля */}
            <div className={styles.inputPassword}>
              <label className={styles.label}>Пароль:</label>
              <input
                type="password"
                className={styles.passwordInputBox}
                placeholder="**********"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {error && <p style={{ color: "red" }}>{error}</p>}
          </div>
          <div className={styles.buttonContainer}>
            {/* Кнопка отправки формы */}
            <button type="submit" className={styles.signInButton}>
              Зарегистрироваться
            </button>
          </div>
        </form>

        {/* Ссылка на авторизацию */}
        <div className={styles.signUpBox}>
          <span>Есть аккаунт?</span>
          <Link href="/auth/signIn" className={styles.signUpText}>
            Войти
          </Link>
        </div>
      </div>
    </div>
  );
}