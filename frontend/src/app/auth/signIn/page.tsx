"use client";

import { useState } from "react";
import Link from 'next/link';
import { useAuth } from '@/app/hooks/useAuth';
import api from '@/app/utils/api';
import { handleApiError } from '@/app/utils/errorHandler';
import styles from './page.module.scss';

export default function SignIn() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();

  const handleSignIn = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);

    try {
      const response = await api.post('/auth/login', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      if (response.status === 200) {
        login(response.data.access_token);
      }
    } catch (error: any) {
      setError(handleApiError(error));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.signInBlock}>
      <div className={styles.formSection}>
        {/* Логотип */}
        <div className={styles.titleBlock}>
          <div className={styles.logo}>Articly</div>
          <span>Войдите в аккаунт, <br/>чтобы продолжить или зарегистрируйтесь</span>
        </div>
        {/* Форма входа */}
        <form onSubmit={handleSignIn}>
          <div className={styles.inputField}>
              {/* Поле ввода Email */}
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

              {/* Поле ввода Пароля */}
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

              <div className={styles.resetPassContainer}>
                {/* Ссылка на сброс пароля */}
                <Link href="./passResetEmail" className={styles.resetPassText}>
                  Забыли пароль?
                </Link>
              </div>
            </div>

            {/* Отображение ошибки */}
            {error && <p style={{ color: "red" }}>{error}</p>}
          <div className={styles.buttonContainer}>
            {/* Кнопка отправки формы */}
            <button type="submit" className={styles.signInButton}>
              Войти
            </button>
          </div>
        </form>

        {/* Ссылка на регистрацию */}
        <div className={styles.signUpBox}>
          <span>Нет аккаунта?</span>
          <Link href="/auth/signUp" className={styles.signUpText}>
            Зарегистрироваться
          </Link>
        </div>
      </div>
    </div>
  );
}