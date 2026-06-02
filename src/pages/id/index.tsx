import type { JSX } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import CursorGlow from "../../components/CursorGlow";

import styles from "../index.module.css";

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Whitepaper dan Dokumentasi Protokol P2P"
    >
      <CursorGlow />
      <header className={clsx("hero", styles.heroBanner)}>
        <div className="container" style={{ position: "relative" }}>
          <h1 className="hero-title">
            Masa Depan <br />
            Koordinasi <span className={styles.highlight}>Terdesentralisasi</span>
          </h1>
          <p className="hero-subtitle">
            Sebuah protokol untuk pertukaran ekonomi yang menjaga privasi,
            tanpa perlu kepercayaan maupun kustodi pihak ketiga.
            Menjembatani kesenjangan antara fiat dan kripto melalui
            reputasi berbasis kredibilitas.
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/id/whitepaper/abstract"
            >
              Baca Dokumentasi
            </Link>
            <Link
              className="button button--secondary button--lg"
              to="https://github.com/p2pdotme/Documentation"
            >
              Lihat di GitHub
            </Link>
          </div>
          <div className={styles.statsRow}>
            <Link
              className="button button--secondary button--lg"
              to="/id/stats"
            >
              Statistik Protokol
            </Link>
          </div>
        </div>
      </header>
    </Layout>
  );
}
