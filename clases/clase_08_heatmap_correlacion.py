# --- 8.3 Heatmap correlación de variables del panel ---
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title("Correlación entre variables (panel departamento-año)")
fig.tight_layout()
fig.savefig(OUT_FIG_DIR / "clase_08_heatmap_correlacion.png")
plt.show()
plt.close(fig)
