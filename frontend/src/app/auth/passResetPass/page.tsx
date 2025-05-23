"use client";

import Link from 'next/link';
import styles from './page.module.scss';
import axios from "axios";
import { useState } from "react"
import { useRouter } from 'next/navigation';

export default function ResetPassPage() {
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState('');

    const handleResetPassword = (e: React.FormEvent) => {
        e.preventDefault();
    };

    return (
        <div className={styles.signInBlock}>
            <div className={styles.formSection}>
                <div className={styles.titleBlock}>
                    <div className={styles.logo}>Articly</div>
                    <span className={styles.Hello}>Восстановление пароля</span>
                    <span className={styles.p}>Пожалуйста, введите Ваш новый пароль <br /> для входа в сервис</span>
                </div>
                <form onSubmit={handleResetPassword}>
                    <div className={styles.inputField}>
                        <div className={styles.inputEmail}>
                            <label className={styles.label}>Новый пароль:</label>
                            <input
                                type="password"
                                className={styles.emailInputBox}
                                placeholder="**********"
                                value={newPassword}
                                onChange={(e) => setNewPassword(e.target.value)}
                                required
                            />
                        </div>
                        <div className={styles.inputPassword}>
                            <label className={styles.label}>Подтверждение пароля:</label>
                            <input
                                type="password"
                                className={styles.passwordInputBox}
                                placeholder="**********"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                required
                            />
                        </div>
                        {error && <p style={{ color: "red" }}>{error}</p>}
                    </div>
                    <div className={styles.buttonContainer}>
                        <button type="submit" className={styles.signInButton}>Изменить пароль</button>
                    </div>
                </form>
                <div className={styles.signUpBox}>
                    <Link href="./signIn" className={styles.signUpText}>Войти в аккаунт</Link>
                </div>
            </div>
        </div>
    )
}