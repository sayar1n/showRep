"use client";

import Link from 'next/link';
import styles from './page.module.scss';
import axios from "axios";
import { useState } from "react"
import { useRouter } from 'next/navigation';

export default function ResetEmailPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState<string | null>(null);
    const router = useRouter();

    const handleResetPassword = (e: React.FormEvent) => {
        e.preventDefault();
    };
    
    {/* Кнопка отправки кода для восстановления пароля */}
    const handleSendCode = () => {
        // Логика отправки кода
    };

    return (
        <div className={styles.signInBlock}>
            <div className={styles.formSection}>
                <div className={styles.titleBlock}>
                    <div className={styles.logo}>Articly</div>
                    <span className={styles.Hello}>Восстановление пароля</span>
                    <span className={styles.p}>Пожалуйста, введите вашу почту, <br />
                        на неё придет код для восстановления</span>
                </div>
                {/* Основная форма регистрации */}
                <form onSubmit={handleResetPassword}>
                    <div className={styles.inputField}>
                        {/* Поле ввода email */}
                        <div className={styles.inputEmail}>
                            <label className={styles.label}>Почта:</label>
                            <div className={styles.emailInputContainer}>
                                <input
                                    type="email"
                                    className={styles.emailInputBox}
                                    placeholder="email@example.com"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    required
                                />
                                <button 
                                    type="button" 
                                    className={styles.sendCodeButton}
                                    onClick={handleSendCode}
                                >
                                    Отправить код
                                </button>
                            </div>
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
                        <button type="submit" className={styles.signInButton}>Продолжить</button>
                    </div>
                </form>
                <div className={styles.signUpBox}>
                    <Link href="./signIn" className={styles.signUpText}>Войти в аккаунт</Link>
                </div>
            </div>
        </div>
    );
}